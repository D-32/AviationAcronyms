import json

# this script converts the file from https://github.com/mwgg/Airports to a smaller json file more suited for us

with open('airfields.json') as json_data:
    data = json.load(json_data)
    newData = {}
    for k, v in data.iteritems(): 
        newData[k] = v['name']

with open('airfields_clean.json', 'w') as f:
    json.dump(newData, f)
