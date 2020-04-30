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


# given a sentence, it finds the rate present in it
def find_rate(sentence):
    final_rate = None
    for rate in kb.rates:
        if rate in sentence:
            final_rate = rate
            break
    return final_rate
