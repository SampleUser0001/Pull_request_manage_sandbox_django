#!/bin/bash

source django_venv/bin/activate
pip install -r requirements.txt

pushd project > /dev/null
python manage.py runserver

popd > /dev/null
