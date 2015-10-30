
import json

# this script converts the data from https://en.wikipedia.org/wiki/List_of_aviation,_aerospace_and_aeronautical_abbreviations into a nice json

newData = {}
with open('acronyms.wiki') as f:
  count = 0
  for line in f:
    count += 1
    if count % 2 == 0:
      parts = line.split('||')
      key = parts[0][1:].strip().replace('<sub>', '').replace('</sub>', '')
      val = parts[1].strip().replace('[[', '').replace(']]', '').replace('|', ' or ')
      newData[key] = val

with open('acronyms_clean.json', 'w') as f:
    json.dump(newData, f)  
      