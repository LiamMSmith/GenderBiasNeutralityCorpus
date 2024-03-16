"""
finetune.py
-----------
This code is used to generate outputs from the fine-tuned gpt3.5 model given a tsv
of the format: source, target.
"""

from openai import OpenAI
client = OpenAI()

# Baseline: gpt-3.5-turbo-0125
# model V1: ft:gpt-3.5-turbo-0125:personal::92xFCGGo
# model V2: ft:gpt-3.5-turbo-0125:personal:test2:93VpopgZ

message_list = []
with open('[FILE_NAME.TSV]', 'r') as file:
  for line in file:
    line = line.split('\t')
    message_list.append(line[0]) # Get src lines
    
for message in message_list:
    completion = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:personal:test2:93VpopgZ",
    messages=[
        {"role": "system", "content": "You are an assistant who corrects sentences for gender bias if it is present."},
        {"role": "user", "content": message}
    ]
    )
    for choice in completion.choices:
        print(choice.message) # Print the output to the console (use terminal to write to correct file)