import json
from sklearn.model_selection import train_test_split

file_path = 'output.jsonl' 

with open(file_path, 'r') as file:
    data = [json.loads(line) for line in file]

train_data, val_data = train_test_split(data, test_size=0.2, random_state=42)

with open('train_data.jsonl', 'w') as file:
    for item in train_data:
        file.write(json.dumps(item) + '\n')

with open('val_data.jsonl', 'w') as file:
    for item in val_data:
        file.write(json.dumps(item) + '\n')

print("Data has been split into training and validation sets and saved.")
