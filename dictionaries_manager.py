import random
from data import knowledge_base as dic


# given a key, it returns randomly one of its value
def find_value(key):
    values = dic.dictionary[key]
    return values[random.randint(0, (len(values)-1))]


# given a sentence, it finds the list of keys present in it
def find_keys(sentence):
    keys_list = []
    for key in dic.dictionary:
        if key in sentence:
            keys_list.append(key)
    return keys_list
