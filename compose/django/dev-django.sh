#!/usr/bin/env bash
python src/website/manage.py migrate
python src/website/manage.py runserver 0.0.0.0:8000
