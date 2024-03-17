"""
compute_BLEU.py
--------------------
This file is used to calculate BLEU scores given a tsv of the 
format: source, target, prediction.
"""

from evaluate import load
import csv

def main(file_name):
    bleu = load("bleu")
    predictions = []
    references = []

    # Get predictions and references
    with open(file_name, 'r') as csv_file:
        tsv_reader = csv.reader(csv_file, delimiter='\t')
        next(tsv_reader)
        for row in tsv_reader:
            predictions.append(row[1])
            references.append([row[2]])
    
    # calculate BLEU score
    results = bleu.compute(predictions=predictions, references=references)
    print(results)

if __name__ == "__main__":
    print("BLEU score for [MODEL_NAME]:")
    main('[FILE_NAME.tsv]')