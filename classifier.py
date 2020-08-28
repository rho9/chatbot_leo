import re
import random
from nltk.stem import PorterStemmer
from data import keywords as kw


# def classifier():
def main():
    stems = find_stems("clever")
    topic = find_topic_counting_words(stems)
    bot_answer = choose_sentence(topic)
    print(bot_answer)


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


def find_topic_counting_words(stems):
    matches = 0
    topic = ""
    for keyword in kw.keywords:
        values = kw.keywords[keyword]
        count = 0
        for value in values:
            if value in stems:
                count += 1
        if count > matches:
            matches = count
            topic = keyword
    print("Final matches:", matches)
    print("Final topic:", topic)
    return topic
    # possiamo mettere gli slot nelle keyword?

def find_topic_use():
    # usa universal_sentece_encoder_tf per trovare il topic
    # messages di là deve diventare il contenuto dei valori di keywords
    # possiamo trascriverli la prima volta e poi tenerli salvati (non ha senso che per ogni
    # rispota io debba andare a aleggermi e scrivermi le frasi)
    return " "


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


def choose_slots(sentence):
    system_file = open("data/sistemi.igrm", "r")
    system = system_file.read()
    system_file.close()
    while "{" in sentence:
        index_left_bracket = sentence.find("{")
        index_right_bracket = sentence.find("}")
        slot = sentence[index_left_bracket:index_right_bracket+1]  # la prima la include, la seconda no
        synonyms = (system.split(slot+" =\n")[1]).split("\n;")[0]
        syn_list = (synonyms.split("\n"))
        # bene così o meglio utilizzare readfile e chiudere il file dopo?
        sentence = sentence.replace(slot, syn_list[random.randint(0, len(syn_list)-1)])
    return sentence


def choose_pipe(sentence):
    while "(" in sentence:
        index_left_bracket = sentence.find("(")
        index_right_bracket = sentence.find(")")
        in_brackets = sentence[index_left_bracket+1:index_right_bracket]
        in_brackets_list = in_brackets.split("|")
        chosen = in_brackets_list[random.randint(0, len(in_brackets_list)-1)]
        sentence = sentence.replace("("+in_brackets+")", chosen)
    return sentence


if __name__ == "__main__":
    main()
