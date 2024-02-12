import json


filename = "resorts.json"

with open(filename, "r") as f:
    resorts = json.loads(f.read())

print(resorts)
