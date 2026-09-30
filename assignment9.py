import csv 
import json

with open("input.csv","r") as file :
   reader = csv.DictReader (file)
   data = list(reader)

with open ("output.json", "w") as file:
  json.dump(data, file, indent=4)

pribnt("CSV file converted to JOSN successfully!")
