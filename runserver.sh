#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
cd app_prompt
exec gunicorn app_prompt.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
