#!/bin/sh

cd /home/ubuntu/nacmis
git checkout master
git pull origin
python manage.py makemigtations data_entry
python manage.py migrate
sudo service apache2 restart
