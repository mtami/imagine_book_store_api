#!/bin/bash

# Navigate to the project root directory
#cd "$(dirname "$0")"/..

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install the latest version of pip
echo "Installing the latest version of pip..."
python3 -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt

# Apply migrations
echo "Apply migrations..."
python3 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear
