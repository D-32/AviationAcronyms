
import json

# this script converts the data from http://www.aopa.org/Pilot-Resources/PIC-archive/Flight-Training-Ratings-and-Proficiency/METAR-TAF-Abbreviations into a nice json

newData = {}
with open('metar.txt') as f:
  count = 0
  key = ""
  value = ""
  for line in f:
    parts = line.split(';')
    newData[parts[0]] = parts[1].replace('\n', '')
    

with open('metar_clean.json', 'w') as f:
    json.dump(newData, f)  
      