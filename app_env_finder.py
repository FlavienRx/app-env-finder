import argparse

import requests
from colorama import Fore, Style
from requests.exceptions import ConnectionError, ConnectTimeout, ReadTimeout

from domains import DOMAINS
from envs import ENVS
from methods import METHODS


def make_call(method, url, timeout):
    try:
        response = requests.request(method, url, timeout=timeout)

    except (ReadTimeout, ConnectTimeout):
        print(Fore.RED, "Timeout", url)
        return

    except ConnectionError:
        print(Fore.RED, "Connection error", url)
        return

    if response.status_code == 404:
        style = Fore.RED

    elif response.status_code == 200:
        style = Fore.GREEN

    else:
        style = Style.RESET_ALL

    print(style, response.status_code, response.reason, method, url)


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
        help="Environement name",
    )
    parser.add_argument(
        "-d",
        "--domain",
        type=str,
        help="Domain name",
    )
    parser.add_argument(
        "-m",
        "--methods",
        action="store_true",
        default=False,
        help="Check all request methods (GET, POST, ...)",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=30,
        help="Request timeout",
    )

    args = parser.parse_args()

    if args.env:
        envs = [args.env]

    else:
        envs = ENVS

    if args.domain:
        domains = [args.domain]

    else:
        domains = DOMAINS

    try:
        for domain in domains:
            for env in envs:
                url = "http://" + env.format(app_name=args.app_name) + "." + domain

                if not args.methods:
                    make_call("GET", url, args.timeout)

                else:
                    for method in METHODS:
                        make_call(method, url, args.timeout)

    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
