from nltk.corpus import wordnet as wn
import random
from data import dictionaries as dic


# it finds the key with biggest weight in the input
# and chooses randomly one of its value as answer
# if none is present, it chooses among default answers
def find_answer(words):
    best_values = []
    for word in words:
        for key in dic.keys_dictionary.keys():
            for syn in wn.synsets(key):
                if word in syn.name():
                    key_values = dic.keys_dictionary[key]
                    key_weight = key_values[0]
                    if best_values == [] or key_weight > best_values[0]:
                        best_values = key_values
    if not best_values:
        none_values = dic.keys_dictionary["none"]
        return none_values[random.randint(1, (len(none_values)-1))]
    else:
        return best_values[random.randint(1, (len(best_values)-1))]


# given a key, it find a value randomly
def find_question(key):
    values = dic.keys_dictionary[key]
    return values[random.randint(1, (len(values)-1))]


# given a list of words, it finds the list of keys present in it
def find_keys(words):
    keys_list = []
    print("words in km", words)
    for word in words:
        if word in dic.keys_dictionary.keys():
            keys_list.append(word)
    return keys_list
