#!/usr/bin/env bash
git pull && ./manage.py migrate && supervisorctl restart dacardio