#!/bin/bash
APP_PORT=${PORT:-8000}

CD /app/

/opt/env/bin/gunicorn --worker-tmp-dir /dev/shm productInventory.wsgi:application --bin "0.0.0.0:${APP_PORT}"