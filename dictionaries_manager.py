from nltk.corpus import wordnet as wn
import random
import input_manager as im
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


# given a key and a dictionary, it find a value randomly among standard questions
def find_value(key, dictionary):
    values = dictionary[key]
    return values[random.randint(0, (len(values)-1))]


# given a key, it calls find_answer with the key and the dictionary about questions
def find_question(key):
    return find_value(key, dic.questions_dictionary)


# given a key, it calls find_answer with the key and the dictionary about concerns
def ask_about_concerns(key):
    return find_value(key, dic.concerns_dictionary)


def ask_situations_dictionary(key):
    return find_value(key, dic.situations_dictionary)


# given a sentence, it finds the list of concerns present in it
def find_concerns(answer):
    keys_list = []
    words = im.tokenize(answer)
    print("words in find_concerns: ", words)
    for word in words:
        if word in dic.concerns_dictionary.keys():
            keys_list.append(word)
    if not keys_list:
        print(find_value("none", dic.concerns_dictionary))
        return find_concerns(input())
    return keys_list

def find_situations(answer):
    key_list = []
    for key in dic.situations_dictionary.keys():
        if key in answer:
            key_list.append(key)
    if not key_list:
        print(find_value("none", dic.concerns_dictionary))
        find_situations(input())
    return key_list
