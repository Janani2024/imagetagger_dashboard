#!/usr/bin/env bash
set -o errexit

pip install setuptools==75.8.2
pip install -r requirements.txt

mkdir -p src/data/images
mkdir -p src/data/tools

cd src
python manage.py collectstatic --no-input
python manage.py migrate
