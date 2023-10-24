import json
import random
import requests

SURNAMES_DATA_URL = 'https://fivethirtyeight.datasettes.com/fivethirtyeight/most-common-name~2Fsurnames.json'
FIRST_NAMES_DATA_URL = 'https://data.cityofnewyork.us/api/views/25th-nujf/rows.json?accessType=DOWNLOAD'

def format_as_name(name):
    return name[0].upper() + name[1:].lower()

def common_surnames():
    r = requests.get(SURNAMES_DATA_URL)
    data = json.loads(r.text)
    return [format_as_name(row['name']) for row in data['rows']]
        
def common_first_names():
    r = requests.get(FIRST_NAMES_DATA_URL)
    data = json.loads(r.text)
    return [format_as_name(row[-3]) for row in data['data']]

class NameGenerator():
    def __init__(self):
        self._surnames = common_surnames()
        self._first_names = common_first_names()

    def __call__(self):
        return (random.choice(self._surnames), random.choice(self._first_names))
