import requests
import json

r = requests.get('')

jsonStruct = r.json()
dumps = json.dumps(jsonStruct, indent=4, sort_keys=True)
loads = json.loads(dumps)
print(loads["value"])
