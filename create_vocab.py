import csv
import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Initialize an empty set for the vocabulary
vocabulary = set()

# Open the .tsv file and read from it
with open('originaldata.tsv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    
    # Skip the header row
    next(reader, None)
    
    # Iterate over the rows in the file
    for row in reader:
        # Check if the row has at least 4 columns
        if len(row) >= 4:
            # Process the third and fourth columns with spaCy to get individual tokens
            doc3 = nlp(row[2])
            doc4 = nlp(row[3])
            
            # Combine the tokens from both columns
            tokens = [token.text for token in doc3] + [token.text for token in doc4]
            
            # Iterate over the tokens and add them to the vocabulary if they are not already present
            for token in tokens:
                if token not in vocabulary:
                    print(token)  # Print the new token
                    vocabulary.add(token)  # Add the new token to the vocabulary
