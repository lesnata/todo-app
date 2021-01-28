# Natalie's pet project: ToDo app
This repository contains Lesna pet project with ToDo app

## Live website: DEPLOY IS ON
Please refer to this link for checking web-site live.
## IMPORTANT
Please be gentle, don't rush. RDS free tier takes time to response


## Brief description
Django RESTful API combined with classic user interface login and to-do list functionality

Users may register and login to their account, views are permission-based.
Token authentification is enabled, stored in cookies at the client-side web-app.

Users can create, update, cross and delete their tasks individually without 
page reloading, thanks to RESTful API URL's triggering.

API functionality:
Initially, URL-mapping was organised poorly, so I've rewritten it according to API best-practices:
without URL actions naming and based on "collection-element" principle.

Separate registration URL provides possibility of Token acquiring and further
request handling.

Deploy:
 


## Technology stack 
- Django;
- Django RESTful API
- JavaScript;
- Bootstrap;
- PostgreSQL deploy on Amazon RDS;
- AWS Elastic Beanstalk

