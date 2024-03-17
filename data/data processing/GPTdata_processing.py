import csv
import json

input_csv_file = 'data.csv'
system_role = "You are an assistant who corrects sentences for gender bias if it is present."


with open(input_csv_file, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        prompt = row[3]
        completion = row[4]
        
        message_structure = {
            "messages": [
                {"role": "system", "content": system_role},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": completion}
            ]
        }
        print(json.dumps(message_structure))
