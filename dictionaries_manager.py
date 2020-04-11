from nltk.corpus import wordnet as wn
import random
import strings_manager as sm
from data import dictionaries as dic


# it finds the key with biggest weight in the input
# and chooses randomly one of its value as answer
# if none is present, it chooses among default answers
# NOT USED AND NOT WORKING: WEIGHT HAS BEEN REMOVED
def find_answer(words):
    best_values = []
    for word in words:
        for key in dic.dictionary.keys():
            for syn in wn.synsets(key):
                if word in syn.name():
                    key_values = dic.dictionary[key]
                    key_weight = key_values[0]
                    if best_values == [] or key_weight > best_values[0]:
                        best_values = key_values
    if not best_values:
        none_values = dic.dictionary["none"]
        return none_values[random.randint(0, (len(none_values)-1))]
    else:
        return best_values[random.randint(0, (len(best_values)-1))]


# given a key and a dictionary, it find a value randomly among standard questions
def find_value(key):
    values = dic.dictionary[key]
    return values[random.randint(0, (len(values)-1))]


# given a sentence, it finds the list of concerns present in it
def find_keys(answer):
    keys_list = []
    for key in dic.dictionary:
        if key in answer:
            keys_list.append(key)
    return keys_list
