# Application Environement Finder

The objective of this project is to find development, staging, and production environments for applications hosted by hosting providers that generate default URLs using the application name.

Example, let's find environments of the 'hello-world' compagny:

```bash
> python app_env_finder.py -a hello-world
502 Bad Gateway GET http://hello-world.herokuapp.com
404 Not Found GET http://hello-world-dev.herokuapp.com
...
404 Not Found GET http://hello-world-front-prod.web.app
404 Not Found GET http://hello-world-front-production.web.app
200 OK GET http://hello-world.netlify.app
404 Not Found GET http://hello-world-dev.netlify.app
...
404 Not Found GET http://hello-world-front-prod.onrender.com
404 Not Found GET http://hello-world-front-production.onrender.com
200 OK GET http://hello-world.vercel.app
404 Not Found GET http://hello-world-dev.vercel.app
...
```

List of domains/hosting providers managed:

- Scalingo:
    - osc-fr1.scalingo.io
    - osc-secnum-fr1.scalingo.io

- Clever Cloud:
    - cleverapps.io

- Firebase:
    - firebaseapp.com
    - web.app

- Netlify
    - netlify.app

- Railway
    - up.railway.app

- Render
    - onrender.com

- Vercel
    - vercel.app

- Deta Space
    - deta.dev

- Pythonanywhere
    - pythonanywhere.com
    - eu.pythonanywhere.com

## Instalation

You can install dependencies with the requirements.txt or with Pipenv

### With requierments.txt

> pip install requierments.txt

### With Pipenv
This project use Pipenv as a virtual environment. You can install Pipenv by following this [link](https://pipenv.pypa.io/en/latest/install/)

Once Pipenv is installed, create a virtual env with Python 3 with this command:
> pipenv shell

To install dependencies, run this command:
> pipenv install


## Run

Get help

> python app_env_finder.py -h

Find environments on all hosting providers

> python app_env_finder.py -a hello-world

Find environments on a specific domains

> python app_env_finder.py -a hello-world -d hosting-provider.com another-hosting-provider.com

Find environments by giving the environment name

> python app_env_finder.py -e hello-world-dev

Find environments by giving the environment names on a specific domains

> python app_env_finder.py -e hello-world-dev hello-world-prod -d hosting-provider.com another-hosting-provider.com

Test all HTTP methods

> python app_env_finder.py -a hello-world -m

Change default timeout

> python app_env_finder.py -a hello-world -t 60

