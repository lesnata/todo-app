## Table of contents
* [General info](#general-info)
* [Live website](#live-website)
* [Brief description](#brief-description)
* [Technologies](#technologies)
* [Deploy](#deploy)
* [Style conventions](#style-conventions)
* [Setup](#setup)

# General Info
This repository contains Lesna pet project with ToDo app

## Live website
Please refer to this link for checking web-site live:
http://todotest-env.eba-6k4zduse.eu-north-1.elasticbeanstalk.com/

## Brief description
Django RESTful API combined with classic user interface login and to-do list functionality

Users may register and login to their account, views are permission-based.
Token authentification is enabled, stored in cookies at the client-side web-app.

Users can create, update, cross and delete their tasks individually without 
page reloading, thanks to RESTful API URL's triggering.
Restrictions are implemented via Token functionality, rest_framework.authtoken package

API functionality:
Initially, URL-mapping was organised poorly, so I've rewritten it according to API best-practices:
without URL actions naming and based on "collection-element" principle.

Separate registration URL provides possibility of Token acquiring and further
request handling.

 
## Technologies 
* Django==3.1.5
* djangorestframework==3.12.2
* Jinja2==2.11.2
* psycopg2-binary==2.8.6
* flake8==3.8.4
* JavaScript;
* Bootstrap;


## Deploy
- PostgreSQL at Amazon RDS;
- AWS Elastic Beanstalk


## Setup
To run this project locally, make the following:

```
$ git clone https://github.com/lesnata/todo-app.git
$ cd todo-app
$ virtualenv venv_todo
$ source venv_todo/bin/activate
$ (venv_todo)$ pip install -r requirements.txt
$ (venv_todo)$ python manage.py runserver
```

