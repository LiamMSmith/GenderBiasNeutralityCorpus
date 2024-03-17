import json

with open('output.json', 'r') as input_file:
    data = input_file.read()

json_strings = data.strip().split('\n')

with open('output.jsonl', 'w') as output_file:
    for json_str in json_strings:
        output_file.write(json_str + '\n')

print("Data has been converted to JSONL format and saved to output.jsonl")