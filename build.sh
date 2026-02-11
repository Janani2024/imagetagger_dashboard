#!/usr/bin/env bash
set -o errexit

pip install setuptools==75.8.2
pip install -r requirements.txt

mkdir -p src/data/images
mkdir -p src/data/tools

cd src
python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created')
else:
    print('Superuser already exists')
"
