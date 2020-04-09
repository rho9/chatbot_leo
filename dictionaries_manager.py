from nltk.corpus import wordnet as wn
import random
from data import dictionaries as dic


# it finds the key with biggest weight in the input
# and chooses randomly one of its value as answer
# if none is present, it chooses among default answers
# NOT USED AND NOT WORKING: WEIGHT HAS BEEN REMOVED
def find_answer(words):
    best_values = []
    for word in words:
        for key in dic.concerns_dictionary.keys():
            for syn in wn.synsets(key):
                if word in syn.name():
                    key_values = dic.concerns_dictionary[key]
                    key_weight = key_values[0]
                    if best_values == [] or key_weight > best_values[0]:
                        best_values = key_values
    if not best_values:
        none_values = dic.concerns_dictionary["none"]
        return none_values[random.randint(0, (len(none_values)-1))]
    else:
        return best_values[random.randint(0, (len(best_values)-1))]


# given a key, it find a value randomly among standard questions
def find_question(key):
    values = dic.questions_dictionary[key]
    return values[random.randint(0, (len(values)-1))]


# given a list of words, it finds the list of concerns present in it
def find_concerns(words):
    keys_list = []
    print("words in km", words)
    for word in words:
        if word in dic.concerns_dictionary.keys():
            keys_list.append(word)
    return keys_list
