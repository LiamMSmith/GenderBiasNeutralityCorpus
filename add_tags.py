import sys
import spacy
from tqdm import tqdm

NLP = spacy.load('en_core_web_sm')

def get_pos_dep(toks):
    def words_from_toks(toks):
        words = []
        word_indices = []
        for i, tok in enumerate(toks):
            words.append(tok.text)
            word_indices.append([i])
        return words, word_indices

    out_pos, out_dep = [], []
    words, word_indices = words_from_toks(toks)
    if len(words) != len(toks):
        return None, None

    for tok, idx in zip(toks, word_indices):
        out_pos += [tok.pos_] * len(idx)
        out_dep += [tok.dep_] * len(idx)
    
    assert len(out_pos) == len(out_dep) == len(toks)
    
    return ' '.join(out_pos), ' '.join(out_dep)

def main(in_file):
    for line in tqdm(open(in_file), total=sum(1 for _ in open(in_file))):
        parts = line.strip().split('\t')
        if len(parts) != 5:
            continue
        sentence = parts[1]  # Assuming parts[1] contains the sentence to be processed.
        toks = [tok for tok in NLP(sentence)]
        pre_pos, pre_dep = get_pos_dep(toks)
        
        if pre_pos is not None and pre_dep is not None:
            print('\t'.join(parts + [pre_pos, pre_dep]))

if __name__ == '__main__':
    in_file = sys.argv[1]
    main(in_file)
