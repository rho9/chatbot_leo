from nltk.corpus import wordnet as wn
import random


keys_dictionary = {
    "test": [2, "test1", "test2", "test3", "test4"],
    "weather": [1, "w1", "w2", "w3", "w4", "w5"]
}


def find_answer(words):
    best_values = []
    for word in words:
        for key in keys_dictionary.keys():
            for syn in wn.synsets(key):
                if word in syn.name():
                    key_values = keys_dictionary[key]
                    key_weight = key_values[0]
                    if best_values == [] or key_weight > best_values[0]:
                        best_values = key_values
    if best_values == []:
        print("I don't know what to say")
    else:
        print(best_values[random.randint(1, (len(best_values)-1))])
