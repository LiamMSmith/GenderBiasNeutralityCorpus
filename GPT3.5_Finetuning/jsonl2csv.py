"""
jsonl2csv.py
------------
This code was used to take the jsonl val_data file and convert it to a tsv file.
"""

import json
import csv

# Open the jsonl file and read it
with open('val_data.jsonl', 'r') as json_file:
    json_list = list(json_file)

# Open the csv file and write to it
# Take the "content" from the "role:user" and put it in one column
# Take the "content" from the "role:assistant" and put it in another column
with open('val_data.tsv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter='\t')
    writer.writerow(["user", "assistant"])
    for json_str in json_list:
        item = json.loads(json_str)
        user = item['messages'][1]['content']
        assistant = item['messages'][2]['content']
        writer.writerow([user, assistant])
    
# Close the csv file
csv_file.close()
