#!/bin/sh

# append secret key to .env
echo "Generate secret key for Django App"
python scripts/generate_random_secret_key.py

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Copy Static files
#echo "gathering static files"
#python manage.py collectstatic --noinput

# Start server
echo "Starting server"
python manage.py runserver
