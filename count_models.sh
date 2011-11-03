#!/bin/bash
python manage.py modelscount  grep da * 2>  $(date +%Y-%m-%d.dat)




