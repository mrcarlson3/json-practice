#!/opt/homebrew/bin/python3.13

import json
import csv


with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)

    
    for i, item in enumerate(data[:5]):  
        csv_writer.writerow([
            item.get("name", ""),
            item.get("html_url", ""),
            item.get("updated_at", ""),
            item.get("visibility", "")
        ])

file.close()
