import random
from data import knowledge_base as kb


# given a key, it returns randomly one of its value
def find_value(key):
    values = kb.dictionary[key]
    return values[random.randint(0, (len(values)-1))]


# given a sentence, it finds the keys present in it
def find_keywords(sentence):
    keywords_list = []
    for keyword in kb.keywords:
        if keyword in sentence:
            keywords_list.append(keyword)
    return keywords_list

