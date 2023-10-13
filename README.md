# Application Environement Finder

The objective of this project is to identify development, staging, and production environments for applications hosted by hosting providers that generate default URLs using the application name.

Example, let's find environnements for the 'hello-world' compagny:

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

- herokuapp.com
- osc-fr1.scalingo.io
- osc-secnum-fr1.scalingo.io
- cleverapps.io
- firebaseapp.com
- web.app
- netlify.app
- up.railway.app
- onrender.com
- vercel.app
- deta.dev
- pythonanywhere.com

## Instalation

You can install dependencies with the requirements.txt or with Pipenv

### With requierments.txt

> pip install requierments.txt

### With Pipenv
This project use Pipenv as a virtual environement. You can install Pipenv by following this [link](https://pipenv.pypa.io/en/latest/install/)

Once Pipenv is installed, create a virtual env with Python 3 with this command:
> pipenv shell

To install dependencies, run this command:
> pipenv install


## Run

Get help

> python app_env_finder.py -h

Find environements on all hosting providers

> python app_env_finder.py -a hello-world

Find environements only on Heroku

> python app_env_finder.py -a hello-world -d herokuapp.com

Find environements by giving the environement name

> python app_env_finder.py -e hello-world-dev

Change default timeout

> python app_env_finder.py -e hello-world-dev -t 60