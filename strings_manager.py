import string
import time
import sys
import nltk
import re


# infer words from user input
def tokenize(user_input):
    sentence = user_input.lower()
    words = sentence.split()
    # remove punctuation
    for word in words:
        for elem in word:
            if elem in string.punctuation:
                word_no_pun = word.replace(elem, "")
                words.remove(word)
                words.append(word_no_pun)  # note: words are no longer in order
    return words


def replace_a_star(sentence, replacement):
    return sentence.replace("*", replacement)


def complete_keywords(sentence, keyword):
    # soft implementation: it takes the string next to the keyword until it finds a dot, a comma or an "and"
    to_add = (sentence.split(keyword)[1]).split("and")[0]
    to_add = to_add.split(",")[0]
    to_add = to_add.split(".")[0]
    modified = keyword + to_add
    return modified


# is it necessary?
def complete_keywords_pos(sentence, keyword):
    # usiamo i tag di nltk invece di usare questo split stupido
    pos = nltk.pos_tag(sentence.split())
    # - vedere se esiste un metodo che li associa in qualche modo, qualcosa che crei una struttura
    # - assegno i tag alle parole
    # - prendo il verbo legato alla parola chiave
    # - prendo la parte dopo legata alla parola chiave
    print(pos)


def my_print_file(file, flag):
    if flag == "slow":
        lines = file.readlines()
        for line in lines:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.09)
        print("\n")
    else:
        print(file.read())


def my_print_string(sentence, flag):
    if flag == "slow":
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.09)
        print()
    else:
        print(sentence)


def is_negative(sentence):
    regex = "no|isn't|didn't|wrong|un"
    negative = re.search(regex, sentence)
    return negative


def create_string_list(list):
    string_list = list[0]
    if len(list) != 1:
        i = 1
        while i < len(list)-1:  # all elements but the last one
            string_list = string_list + ", " + list[i]
            i += 1
        string_list = string_list + " and " + list[i]
    return string_list