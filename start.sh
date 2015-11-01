#!/bin/bash

# A script to run by yourself the blog.
# Not used during the presentation
# Dependancies :
# - Python 3
# - virtualenv


# Creating the virtualenv
virtualenv -q virtualenv

# We use the virtualenv
source ./virtualenv/bin/activate

# We install all the requirements
pip install -r requirements.txt

# If you have any tests 
#python manage.py test blogengine

# We create all the migrations for the changes in the models.py file
python manage.py makemigrations

# We apply the migrations created previously
python manage.py migrate

# We compile all the translation files 
python manage.py compilemessages

# We run the server
python manage.py runserver
