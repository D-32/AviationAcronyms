
import json

# this script converts the data from http://www.moratech.com/aviation/notam-abbrev.html into a nice json

newData = {}
with open('notam.txt') as f:
  count = 0
  key = ""
  value = ""
  for line in f:
    count += 1
    if count % 6 == 1:
      key = line
    if count % 6 == 3:
      value = line
    if count % 6 == 5:
        newData[key] = value
    

with open('notam_clean.json', 'w') as f:
    json.dump(newData, f)  
      