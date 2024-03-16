"""
compute_bertscore.py
--------------------
This file is used to calculate bertscore precision, accuracy, and F1 given a 
tsv of the format: source, target, prediction.
"""

from evaluate import load
from bert_score import score
import csv

def main(file_name):
    predictions = []
    references = []

    # Get predictions and references
    with open(file_name, 'r') as csv_file:
        tsv_reader = csv.reader(csv_file, delimiter='\t')
        next(tsv_reader)
        for row in tsv_reader:
            predictions.append(row[1])
            references.append(row[2])
    
    # calculate BLEU score
    P, R, F1 = score(predictions, references, lang='en', verbose=True)
    print("System Precision: ", P.mean())
    print("System Recall: ", R.mean())
    print("System F1: ", F1.mean())

if __name__ == "__main__":
    print("bertscore for [MODEL_NAME]:")
    main('[FILE_NAME.tsv]')