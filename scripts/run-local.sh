#!/bin/sh

# append secret key to .env
echo "Generate secret key for Django App"
python scripts/generate_random_secret_key.py

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Copy Static files
echo "gathering static files"
python manage.py collectstatic --noinput


# Check if the script is run as root or with sudo privileges
if [ "$(id -u)" != "0" ]; then
  echo "This script must be run as root or with sudo."
  exit 1
fi

# Run the script to kill processes on port 8000 as a subprocess
echo "Running the script to kill processes on port 8000..."
bash scripts/kill_port_8000.sh

# Start server
echo "Starting server"
#python manage.py runserver
gunicorn --workers 2 --bind :8000 core.wsgi
