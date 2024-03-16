"""
text2csv.py
-----------
This code was used to take the output from finetune.py, run the clean() function on it 
to format it properly, and then add together with the original val_data set to get
a tsv file of the format: source, target, prediction. This file is then used to generate
BLEU scores and bertscores.
"""

import csv

"""
For each line in output.txt extract the content.
Remove single quotes wrapped around the line.
"""
def clean():
    with open('[UNPROCESSED_DATA.txt]', 'r') as file:
        lines = file.readlines()
    with open('[PROCESSED_DATA.txt]', 'w') as file:
        for line in lines:
            line = line.split("(content=")[1]
            line = line.split(", role=")[0]
            if line.startswith("'"):
                line = line[1:]
            if line.endswith("'"):
                line = line[:-1]
            file.write(line + '\n')

"""
Prepares data for BLEU score and bertscore calculation. Read in a 
dataset of the format (source, target) and a text file whose columns are predictions, 
and write to a new file with the format (source, target, predictions).
"""
def main():
    # Open the tsv file and read from it
    with open('[FILE_NAME.tsv]', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        csv_list = list(csv_reader)

    # Open the predictions file and read from it
    with open('[PROCESSED_DATA.txt]', 'r') as output_file:
        output_list = output_file.readlines()

    # Open the output file and write to it
    with open('[OUTPUT_NAME.tsv]', 'w', newline='') as finetune_file:
        writer = csv.writer(finetune_file, delimiter='\t')
        writer.writerow(["src", "tgt", "baseline_output"])
        for i in range(len(csv_list)):
            user = csv_list[i][0]
            assistant = csv_list[i][1]
            content = output_list[i].strip()
            writer.writerow([user, assistant, content])

    # Close the csv file
    csv_file.close()
    # Close the output file
    output_file.close()
    # Close the finetune file
    finetune_file.close()

if __name__ == "__main__":
    clean() # Clean the output file
    main()