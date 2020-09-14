#!/bin/bash

python -m venv ../venv;
source ../venv/bin/activate;
pip install django;
pip install djangorestframework
pip install validator-collection;
pip install decorators
python manage.py makemigrations;
python manage.py migrate;
python manage.py runserve;
