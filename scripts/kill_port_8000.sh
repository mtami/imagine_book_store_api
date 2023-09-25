#!/bin/bash

# Check if the script is run as root or with sudo privileges
if [ "$(id -u)" != "0" ]; then
  echo "This script must be run as root or with sudo."
  exit 1
fi

# Find processes listening on port 8000 using lsof
echo "Finding processes listening on port 8000..."
PIDS=$(lsof -ti :8000)

if [ -z "$PIDS" ]; then
  echo "No processes found listening on port 8000."
else
  # Kill the processes
  echo "Killing processes on port 8000..."
  for PID in $PIDS; do
    kill -9 "$PID"
    echo "Killed process $PID."
  done
fi

echo "Done."
