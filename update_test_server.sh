#!/bin/sh

cd /home/ubuntu/nacmis
git checkout master
git pull origin
/home/ubuntu/.virtualenvs/nacmis/bin/python3 manage.py makemigrations --noinput
/home/ubuntu/.virtualenvs/nacmis/bin/python3 manage.py collectstatic
/home/ubuntu/.virtualenvs/nacmis/bin/python3  manage.py migrate
sudo service apache2 restart
