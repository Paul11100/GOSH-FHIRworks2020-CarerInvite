import requests

#Api Endpoint
URL = "http://127.0.0.1:5002/patients"

# Params
limit = 3
lower = 55
upper = 65
name = "Paul"
ref = "UCL-FHIR-Hack"
url = "appdownload.com"

PARAMS = {'limit':limit, 'lower':lower, 'upper':upper, 'name':name, 'ref':ref, 'url':url}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

for patient in data:
    print(patient["phone"])
    print(patient["msg"])
    print()

