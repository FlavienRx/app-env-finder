#!/usr/bin/python3

import argparse

import requests
from requests import Response
from colorama import Fore, Style
from requests.exceptions import ConnectionError, ConnectTimeout, ReadTimeout

from domains import DOMAINS
from envs import ENVS
from methods import METHODS


def send_request(method: str, url: str, timeout: int) -> Response or None:
    try:
        return requests.request(method, url, timeout=timeout)

    except (ReadTimeout, ConnectTimeout):
        print(Fore.RED, "Timeout", url)

    except ConnectionError:
        print(Fore.RED, "Connection error", url)


def show_response(
    response: Response,
    method: str,
    url: str,
    hide_code: list[int],
) -> None:
    if response.status_code in hide_code:
        return

    elif response.status_code == 404:
        style = Fore.RED

    elif 200 <= response.status_code < 300:
        style = Fore.GREEN

    else:
        style = Style.RESET_ALL

    print(style, response.status_code, response.reason, method, url)


def run(
    app_name: str,
    envs: list[str],
    domains: list[str],
    methods: list[str],
    timeout: int,
    hide_code: list[int],
) -> None:
    for env in envs:
        for domain in domains:
            url = "http://" + env.format(app_name=app_name) + "." + domain

            for method in methods:
                response = send_request(method, url, timeout)

                if response is not None:
                    show_response(response, method, url, hide_code)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-a",
        "--app-name",
        type=str,
        help="App name to generate environements list",
    )
    group.add_argument(
        "-e",
        "--env",
        type=str,
        nargs="+",
        help="Environement name",
    )
    parser.add_argument(
        "-d",
        "--domain",
        type=str,
        nargs="+",
        help="Domain name",
    )
    parser.add_argument(
        "-m",
        "--methods",
        type=str,
        nargs="*",
        choices=METHODS,
        default=None,
        help="Test request methods, empty value will test all methods",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=30,
        help="Request timeout",
    )
    parser.add_argument(
        "-H",
        "--hide-code",
        type=int,
        nargs="+",
        default=[],
        help="Hide HTTP response codes",
    )

    args = parser.parse_args()

    envs = args.env if args.env else ENVS
    domains = args.domain if args.domain else DOMAINS

    if args.methods is None:
        methods = ["GET"]

    elif not args.methods:
        methods = METHODS

    else:
        methods = args.methods

    try:
        run(args.app_name, envs, domains, methods, args.timeout, args.hide_code)
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
