import string
import time
import sys


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


def my_print(speech, flag):
    if flag == "slow":
        lines = speech.readlines()  # problem: it works with file, but sometimes I have strings
        for line in lines:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.07)
            print(speech.read())
    else:
        print(speech.read())
