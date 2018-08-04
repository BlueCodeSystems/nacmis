#!python

import json
import os

from django.core.management.base import BaseCommand, CommandError
#from polls.models import ...

import requests


def get_credentials():
    whereami = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(whereami, "credentials.txt")
    if os.path.exists(path):
        with open(path) as f:
            login = f.readline().strip()
            password = f.readline().strip()
            return (login, password)
    else:
        raise OSError("File does not exist: %s" % path)

class DHIS2Error(Exception):
    pass

class DHIS2:
    LOGIN_URL = "https://play.dhis2.org/2.30/dhis-web-commons/security/login.action"
    API_URL = "https://play.dhis2.org/demo/api/dataValueSets.json"

    def __init__(self, login, password):
        self.sess = requests.Session()
        self.logged_in = False
        self.cookies = {}
        self.login(login, password)

    def login(self, login, password):
        r = self.sess.post(self.LOGIN_URL, auth=(login, password))
        #print(r.status_code)
        #print(r.headers)
        #print(r.encoding)
        #print(r.cookies)
        import pprint; pprint.pprint(r.__dict__)
        if r.status_code == 200:
            print("Succesfully logged in.")
            self.logged_in = True
            self.cookies = r.cookies
        else:
            print("** Login failed")
            print(r.status_code)
            print(r.headers)
            print(r.cookies)
            print(r.text)
            raise DHIS2Error("Could not login")
        

class Command(BaseCommand):
    def handle(self, *args, **options):
        login, password = get_credentials()
        dhis2 = DHIS2(login, password)
        if dhis2.logged_in:
            r2 = dhis2.sess.get(dhis2.API_URL, cookies=dhis2.cookies, 
                          headers={'Content-Type': 'application/json'}, 
                          params={'orgUnit': "DiszpKrYNg8", 'period': '201801',
                                  'dataSet': 'BfMAe6Itzgt'})
            print(r2.url)
            print(r2.status_code)
            print(r2.headers)
            print(r2.encoding)
            j = r2.json()
            print(json.dumps(j, sort_keys=True, indent=4))

