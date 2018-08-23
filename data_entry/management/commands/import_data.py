#!python

import json
import os

from django.core.management.base import BaseCommand, CommandError
#from polls.models import ...

import requests


def get_credentials():
    """ Read credentials from a file credentials.txt that must be located in the
        same directory as this file. It's a simple text file; the first line
        contains the login, the second the password. 
    """
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
class HMISError(Exception):
    pass


class DHIS2:
    API_BASE_URL = "https://play.dhis2.org/demo/api/"
    LOGIN_URL = "https://play.dhis2.org/2.30/dhis-web-commons/security/login.action"
    API_URL = "https://play.dhis2.org/demo/api/dataValueSets.json"

    def __init__(self, login, password):
        self.sess = requests.Session()
        self.logged_in = False
        self.cookies = {}
 
        # cached values
        self.orgUnits = []

        self.login(login, password)

    def login(self, login, password):
        print("Logging in...")
        r = self.sess.post(self.LOGIN_URL, auth=(login, password))
        #print(r.status_code)
        #print(r.headers)
        #print(r.encoding)
        #print(r.cookies)
        #import pprint; pprint.pprint(r.__dict__)
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

    def getPagedResults(self, url, name):
        """ Get results from an API calls, taking into account that there might
            be multiple pages. If there are, fetch all those pages and return
            the combined results.
        """

        def getPageResult(page):
            print("  Fetching page %s..." % page)
            r = self.sess.get(url, cookies=self.cookies, 
                              params={'page': page},
                              headers={'Content-Type': 'application/json'})
            return r.json()

        page = 1
        results = []

        while True:
            j = getPageResult(page)
            results.extend(j[name])
            pager = j['pager']
            # if we reached the last page, break out of the loop
            if pager['page'] >= pager['pageCount']:
                print("All pages fetched")
                break
            page += 1

        return results
        
    def getOrgUnits(self):
        """ Get a list of organisation units. This is a list of dictionaries
            like:

            {
                "displayName": "Adonkia CHP",
                "id": "Rp268JB6Ne4"
            }
        """
        print("Loading organisation units...")
        URL = self.API_BASE_URL + "organisationUnits.json"
        self.orgUnits = self.getPagedResults(URL, 'organisationUnits')
        print("%s organisationunits found" % len(self.orgUnits))


class ZambiaHMIS:
    ORG_UNIT_API = "https://www.zambiahmis.org/api/organisationUnits.json?paging=false"
    LOGIN_URL = "https://www.zambiahmis.org/dhis-web-commons/security/login.action"

    def __init__(self, login, password):
        self.sess = requests.Session()
        self.logged_in = False
        self.cookies = {}
 
        # cached values
        self.orgUnits = []

        self.login(login, password)

    def login(self, login, password):
        print("Logging in...")
        r = self.sess.post(self.LOGIN_URL, auth=(login, password))
        #print(r.status_code)
        #print(r.headers)
        #print(r.encoding)
        #print(r.cookies)
        #import pprint; pprint.pprint(r.__dict__)
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

    # XXX maybe rename to getResults?
    def getPagedResults(self, url, name, paged=True):
        """ Get results from an API calls, taking into account that there might
            be multiple pages. If there are, fetch all those pages and return
            the combined results.
        """

        def getPageResult(page):
            print("  Fetching page %s..." % page)
            r = self.sess.get(url, cookies=self.cookies, 
                              params={'page': page},
                              headers={'Content-Type': 'application/json'})
            return r.json()

        page = 1
        results = []

        if not paged:
            j = getPageResult(page)
            return j[name]

        while True:
            j = getPageResult(page)
            results.extend(j[name])
            pager = j['pager']
            # if we reached the last page, break out of the loop
            if pager['page'] >= pager['pageCount']:
                print("All pages fetched")
                break
            page += 1

        return results

    def getOrgUnits(self):
        """ Get a list of organisation units. This is a list of dictionaries
            like:

            {
                "displayName": "Adonkia CHP",
                "id": "Rp268JB6Ne4"
            }
        """
        print("Loading organisation units...")
        self.orgUnits = self.getPagedResults(self.ORG_UNIT_API, 'organisationUnits', 
                                             paged=False)
        print("%s organisation units found" % len(self.orgUnits))


class Command(BaseCommand):

    def handle(self, *args, **options):
        login, password = get_credentials()
        hmis = ZambiaHMIS(login, password)
        if hmis.logged_in:
            hmis.getOrgUnits()
            return

        # unclear how to proceed from here...
        '''
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
        '''

