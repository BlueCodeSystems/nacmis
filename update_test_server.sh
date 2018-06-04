#!/bin/sh

cd /home/ubuntu/nacmis
git checkout master
git pull origin
pip freeze > requirements.txt
/home/ubuntu/.virtualenvs/nacmis/bin/python3 manage.py makemigrations --noinput
/home/ubuntu/.virtualenvs/nacmis/bin/python3  manage.py migrate
sudo service apache2 restart
