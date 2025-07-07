import pandas as pd
import os

DICT_PATH = os.path.join(os.path.dirname(__file__), '../data/dictionary.csv')

def load_dictionary():
    return pd.read_csv(DICT_PATH)

dictionary = load_dictionary()

def find_words_by_ipa(ipa_fragment, language):
    matches = dictionary[
        (dictionary['language'] == language) &
        (dictionary['ipa'].str.contains(ipa_fragment))
    ]
    return matches['word'].tolist()
