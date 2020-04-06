from nltk.corpus import wordnet as wn
import random
from data import keys_dictionary as kd


# it prints the key with biggest weight in the input
# and chooses randomly one of its value as answer
# if none is present, it chooses among default answers
def print_answer(words):
    best_values = []
    for word in words:
        for key in kd.keys_dictionary.keys():
            for syn in wn.synsets(key):
                if word in syn.name():
                    key_values = kd.keys_dictionary[key]
                    key_weight = key_values[0]
                    if best_values == [] or key_weight > best_values[0]:
                        best_values = key_values
    if not best_values:
        none_values = kd.keys_dictionary["none"]
        print(none_values[random.randint(1, (len(none_values)-1))])
    else:
        print(best_values[random.randint(1, (len(best_values)-1))])


# given a key, it prints a value randomly
def print_question(key):
    values = kd.keys_dictionary[key]
    print(values[random.randint(1, (len(values)-1))])


# given a list of words, it finds the list of keys present in it
def find_keys(words):
    keys_list = []
    print("words in km", words)
    for word in words:
        if word in kd.keys_dictionary.keys():
            keys_list.append(word)
    return keys_list
