import requests
import json
import pprint

from datetime import date, timedelta


today = date.today()

yesterday = today - timedelta(days=1)

country = "united states"

endpoint = "https://api.covid19api.com/country/{}/status/confirmed".format(country)

#print(endpoint)

params = {"from": str(yesterday), "to": str(today)}


response = requests.get(endpoint, params=params).json()

total_confirmed = 0

for day in response:

    cases = day.get("Cases", 0)

    total_confirmed += cases


#parsed = json.load(response)

pprint.pprint(response)