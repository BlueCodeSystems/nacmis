#!python

import json

from django.core.management.base import BaseCommand, CommandError
#from polls.models import ...

import requests

LOGIN_URL = "https://play.dhis2.org/2.30/dhis-web-commons/security/login.action"
API_URL = "https://play.dhis2.org/demo/api/dataValueSets.json"

# test credentials -- put real site credentials somewhere else!!
USERNAME = "admin"
PASSWORD = "district"

class Command(BaseCommand):
    def handle(self, *args, **options):
        sess = requests.Session()
        r = sess.post(LOGIN_URL, auth=(USERNAME, PASSWORD))
        print(r.status_code)
        print(r.headers)
        print(r.encoding)
        print(r.cookies)
        import pprint; pprint.pprint(r.__dict__)
        if r.status_code == 200:
            print("Succesfully logged in.")
            r2 = sess.get(API_URL, cookies=r.cookies, 
                          headers={'Content-Type': 'application/json'}, 
                          params={'orgUnit': "DiszpKrYNg8", 'period': '201801',
                                  'dataSet': 'BfMAe6Itzgt'})
            print(r2.url)
            print(r2.status_code)
            print(r2.headers)
            print(r2.encoding)
            j = r2.json()
            print(json.dumps(j, sort_keys=True, indent=4))
