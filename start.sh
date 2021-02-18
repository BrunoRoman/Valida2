#!/bin/bash

celery -A valida worker -l info --concurrency=4 &
python manage.py runserver

