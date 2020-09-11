import re
import random
from nltk.stem import PorterStemmer
from data import keywords as kw
from embedding import universal_sentence_encoder_tf as use_tf


# def classifier():
def main():
    print("### COUNTER ###")
    stems = find_stems("clever")
    topic_counter = find_topic_counting_words(stems)
    bot_answer = choose_sentence(topic_counter)
    print(bot_answer)
    print("\n### UNIVERSAL SENTENCE ENCODER ###")
    topic_use = find_topic_use("I'm afraid to sound stupid", )
    bot_answer = choose_sentence(topic_use)
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


def find_topic_use(sentence, situation):
    # possiamo trascriverli la prima volta e poi tenerli salvati (non ha senso che per ogni
    # rispota io debba andare a aleggermi e scrivermi le frasi)
    messages = use_tf.update_messages([])
    dictionary_value = use_tf.run_use(messages, sentence)
    if dictionary_value == "Threshold issue":
        topic = under_threshold(situation)
    else:
        topic = get_key(dictionary_value)
    print("######### Topic:", topic)
    return topic


def get_key(val):
    for key, values in kw.keywords.items():
        for value in values:
            if val == value:
                return key
    return "key doesn't exist"


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


# non ci siamo: io voglio nuove entry, ma ora reagisco come se le avessi appena avute invece di
# chiederle
# vedere se abbiamo delle frasi da qualche parte che li chiedono o creare due nuove grammatiche
def under_threshold(situation):
    # qua dobbiamo valutare cosa abbiamo imparato e decidere se passare alla sessione 2
    # o se fare una delle domande per rimpinguare cosa è scarno
    # se physical symptoms length < 5
    # domanda sui phy_sym
    # se safety behaviours < 4
    # domanda sui safe_behav
    # altirmenti andiamo alla sessione 2
    if len(situation.get_physical_symptoms()) < 5:
        # è meglio dire a s1 di chiedere riguardo ai phy_sym perché altirmenti dobbiamo
        # poi ritornare anche situations. se è solo per quello si può fare, ma bisogna valutare se
        # si scombussola anche altro
        # di là si aspettano un topic, quidni la cosa più semplice  mandargli il topic di
        # phy_sym piuttosto che dei safe_behav e hai finito..così se la sbrigano poi di là
        print("Threshold basso, voglio più sintomi fisici")
        return "ask_about_phy_sym"
    if len(situation.get_safety_behaviours()) < 4:
        print("Threshold basso, voglio più comportamenti di difesa")
        return "ask_about_safe_behav"
    print("Threshold basso, ma ho tutto quello che mi serve")
    return "enough"


if __name__ == "__main__":
    main()
