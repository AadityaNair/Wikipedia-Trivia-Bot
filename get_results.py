#!/usr/bin/env python3
# Code to retrieve data from SPARQL endpoint

from requests import get
from pprint import pprint

url = 'http://dbpedia.org/sparql'
params = {
        'default-graph-uri':'http://dbpedia.org',
        'format':'application/sparql-results+json'
        }
def query(sparql):
    params['query'] = sparql
    response = get(url, params)
    print(response.json())
    ans = response.json()['results']['bindings']
    pprint(ans)
