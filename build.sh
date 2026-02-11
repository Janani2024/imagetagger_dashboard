#!/usr/bin/env bash
set -o errexit

pip install setuptools>=75.0
pip install -r requirements.txt

mkdir -p src/data/images
mkdir -p src/data/tools

cd src
python manage.py collectstatic --no-input
python manage.py migrate
