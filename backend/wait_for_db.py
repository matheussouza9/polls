#!/usr/bin/env python
from __future__ import absolute_import

import os
import time

import django
from django.db import connections
from django.db.utils import OperationalError

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    connected = False
    while not connected:
        try:
            django.setup()
            db_conn = connections["default"]
            c = db_conn.cursor()
            connected = True

        except OperationalError:
            print("Waiting for database...")
            time.sleep(1)

    exit(0)
