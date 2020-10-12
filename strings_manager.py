import time
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import kb_manager as kbm


# infer words from user input
def tokenize(sentence):
    sentence = sentence.lower()
    word_tokens = word_tokenize(sentence)
    tokenized_sentence = [w for w in word_tokens if w not in stopwords.words('english')]
    return tokenized_sentence


def replace_a_star(sentence, replacement):
    return sentence.replace("*", replacement)


# take the string next to the keyword until it finds a dot, a comma or an "and"
def complete_keywords(sentence, keyword):
    to_add = (sentence.split(keyword)[1]).split("and")[0]
    to_add = to_add.split(",")[0]
    to_add = to_add.split(".")[0]
    modified = keyword + to_add
    return modified


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


# it creates the summary that must be printed in session 2
def create_string_list(list):
    string_list = list[0]
    if len(list) != 1:
        i = 1
        while i < len(list)-1:  # all elements but the last one
            string_list = string_list + ", " + list[i]
            i += 1
        string_list = string_list + ", and " + list[i]
    return string_list


def add_particles(reaction, keyword):
    composed_sentence = ""
    if "thoughts1" in keyword:
        reaction = to_second_person(reaction)
        composed_sentence = "you are worried they " + reaction
    elif "thoughts2" in keyword:
        reaction = to_second_person(reaction)
        composed_sentence = "you are worried to seem " + reaction
    elif "thoughts3" in keyword:
        reaction = to_second_person(reaction)
        composed_sentence = "you are worried that " + reaction
    elif "phys1" in keyword:
        reaction = to_second_person(reaction)
        composed_sentence = "you become " + reaction
    elif "phys2" in keyword:
        reaction = to_second_person(reaction)
        composed_sentence = "you start " + reaction
    elif "phys3" in keyword or "sft" in keyword or "focus" in keyword or "sit" in keyword:
        reaction = to_second_person(reaction)
        composed_sentence = "you " + reaction
    return composed_sentence


def add_particles_from_topic(reaction):
    typology = kbm.find_typology(reaction)
    replacement = ""
    if typology == "phys1":
        replacement = "become " + reaction
    elif typology == "phys2":
        replacement = "start " + reaction
    elif typology == "phys3":
        replacement = reaction
    return replacement


def to_second_person(reaction):
    reaction = reaction.replace("I ", "you ")
    reaction = reaction.replace(" me", " you")
    reaction = reaction.replace(" my", " your")
    return reaction


def find_stems(sentence):
    ps = PorterStemmer()
    # were e was non li rende is, ma chissene..non sono keywords..magari fai un check sulle keywords
    sentence = sentence.lower()
    words = sentence.split()
    sentence_stems = ""
    for word in words:
        if sentence_stems:
            sentence_stems = sentence_stems + " " + ps.stem(word)
        else:  # the first time the white space must not be present
            sentence_stems = sentence_stems + ps.stem(word)
    print("find_stems:", sentence_stems)
    return sentence_stems
