import time
import sys
import re
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import kb_manager as kbm


# it infers tokens from user input
def tokenize(sentence):
    sentence = sentence.lower()
    word_tokens = word_tokenize(sentence)
    tokenized_sentence = [w for w in word_tokens if w not in stopwords.words('english')]
    return tokenized_sentence


# it replaces the star * with the string in replacement
def replace_a_star(sentence, replacement):
    return sentence.replace("*", replacement)


# it takes the words next to the keyword until it finds an "and", a comma, or a dot
def complete_keywords(sentence, keyword):
    to_add = (sentence.split(keyword)[1]).split("and")[0]
    to_add = to_add.split(",")[0]
    to_add = to_add.split(".")[0]
    modified = keyword + to_add
    return modified


# if the flag is slow, it prints the sentences as if someone was typing
# otherwise it prints the file normally
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


# if the flag is slow, it prints the sentences as if someone was typing
# otherwise it prints the string normally
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


# it adds the needed particles to the given reactions
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


# it changes the first person in user's sentence to the second person
def to_second_person(reaction):
    reaction = reaction.replace("I ", "you ")
    reaction = reaction.replace(" me", " you")
    reaction = reaction.replace(" my", " your")
    return reaction


# it returns sentence stems
def find_stems(sentence):
    ps = PorterStemmer()
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


# it takes a sentence from the given topic
def choose_sentence(topic):
    grm = open("data/grammar/" + topic + ".grm", "r")
    topic_file = grm.read()
    grm.close()
    sentences = (topic_file.split(";")[1])
    sentences_list = re.findall("{topic}.+", sentences)
    # . -> Any character (except newline character)
    # + -> One or more occurrences
    sentence = sentences_list[random.randint(0, len(sentences_list)-1)]
    sentence = sentence[7:len(sentence)]  # remove {topic}
    sentence = choose_optional(sentence)
    sentence = choose_slots(sentence)
    sentence = choose_pipe(sentence)
    return sentence


# it decides whether to keep the string between the brackets
def choose_optional(sentence):
    while "[" in sentence:
        index_left_bracket = sentence.find("[")
        index_right_bracket = sentence.find("]")
        in_brackets = sentence[index_left_bracket+1:index_right_bracket]
        include = random.randint(0, 1)
        if include:
            sentence = sentence.replace("[" + in_brackets + "]", in_brackets)
        else:
            sentence = sentence.replace("[" + in_brackets + "]", "")
    return sentence


# it chooses an appropriate slot to be replaced
def choose_slots(sentence):
    system_file = open("data/sistemi.igrm", "r")
    system = system_file.read()
    system_file.close()
    while "{" in sentence:
        index_left_bracket = sentence.find("{")
        index_right_bracket = sentence.find("}")
        slot = sentence[index_left_bracket:index_right_bracket+1]
        synonyms = (system.split(slot+" =\n")[1]).split("\n;")[0]
        syn_list = (synonyms.split("\n"))
        sentence = sentence.replace(slot, syn_list[random.randint(0, len(syn_list)-1)])
    return sentence


# it chooses which part of the string in brackets to keep
def choose_pipe(sentence):
    while "(" in sentence:
        index_left_bracket = sentence.find("(")
        index_right_bracket = sentence.find(")")
        in_brackets = sentence[index_left_bracket+1:index_right_bracket]
        in_brackets_list = in_brackets.split("|")
        chosen = in_brackets_list[random.randint(0, len(in_brackets_list)-1)]
        sentence = sentence.replace("("+in_brackets+")", chosen)
    return sentence
