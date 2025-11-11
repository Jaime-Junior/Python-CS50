#Run with "python api.py 1_WORD_NAME"
#Doc: https://swapi.dev/documentation

import json
import requests
import sys

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://swapi.dev/api/people/?search=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2)) #Whole response

name = response.json()
for result in name["results"]:
    print(result["name"])