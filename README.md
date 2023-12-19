# Recipe App

## Description

A recipe app developed using Django framework, deployed on Heroku.

<img src="/media/homepage.jpg" alt ="A screenshot of home page" width="400">
<img src="/media/login.jpg" alt ="A screenshot of login page" width="400">
<img src='/media/detail.jpg' alt ='A screenshot of recipe detail' width='400'>
  
Deployed app: https://obscure-reaches-05845-5c9fc5ba382e.herokuapp.com/

## Features

- Login to view list of recipes.
- User able to click on respective recipe to view more details on description, cooking time, difficulty and ingredients.

## Dependencies

- Python
- Django

## Installation

1. Clone repo

- ` git clone https://github.com/joannawongww/recipeapp-deploy2`

2. Install requirements

- `pip install -r requirements.txt`

3. Migrate the database

- `python manage.py migrate`

4. Run local server

- `python manage.py runserver`
