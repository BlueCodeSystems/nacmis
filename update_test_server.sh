#!/bin/sh

cd /home/ubuntu/nacmis
git checkout master
git pull origin
sudo service apache2 restart
