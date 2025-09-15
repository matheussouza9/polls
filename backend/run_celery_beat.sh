#!/usr/bin/env bash

until python wait_for_db.py; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

rm -f celerybeat.pid celerybeat-schedule
celery -A config beat -l warning --scheduler django_celery_beat.schedulers:DatabaseScheduler