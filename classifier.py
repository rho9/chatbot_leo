import re
import random
from nltk.stem import PorterStemmer
from data import keywords as kw
from embedding import universal_sentence_encoder_tf as use_tf
from datetime import datetime
from embedding import glove_cosine_similarity as glove


# def classifier():
def main():
    sentence = "My anxiety is been stopping me a bit from being able to get work"
    print("Sentence to be analyze:", sentence)
    now = datetime.now()

    # load glove
    glove_model = glove.load_glove_model()
    messages = use_tf.update_messages([])

    print("### COUNTER ###")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("Start time =", current_time)
    stems = find_stems(sentence)
    topic_counter = find_topic_counting_words(stems)
    print("Topic counter:", topic_counter)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("End time =", current_time)

    print("\n### UNIVERSAL SENTENCE ENCODER ###")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("Start time =", current_time)
    topic_use = find_topic_use(sentence, "")
    print("Topic use:", topic_use)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("End time =", current_time)

    print("\n### GLOVE ###")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("Start time =", current_time)
    topic_glove = find_topic_glove(sentence, "", glove_model, messages)
    print("Topic glove:", topic_glove)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("End time =", current_time)


def find_topic(sentence, situation, method):
    topic = ""
    if method == "counter":
        stems = find_stems("sentence")
        topic = find_topic_counting_words(stems)
    elif method == "glove":
        topic = "da fare"
    elif method == "use":
        topic = find_topic_use(sentence, situation)
    return topic


# mettere in string_manager
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
    for keyword in kw.keywords_count:
        values = kw.keywords_count[keyword]
        count = 0
        for value in values:
            if value in stems:
                count += 1
        if count > matches:
            matches = count
            topic = keyword
    # print("Final matches:", matches)
    # print("Final topic:", topic)
    print("Number of stems found =", matches)
    return topic
    # possiamo mettere gli slot nelle keyword?


def find_topic_use(sentence, situation):
    # possiamo trascriverli la prima volta e poi tenerli salvati (non ha senso che per ogni
    # rispota io debba andare a aleggermi e scrivermi le frasi)
    messages = use_tf.update_messages([])
    dictionary_value = use_tf.run_use(messages, sentence)
    topic = ""
    if dictionary_value == "Threshold issue":
        if situation == "":  # if inserito per fare il test tra i tre
            topic = "low threshold"
        else:
            topic = under_threshold(situation)
    else:
        topic = get_key(dictionary_value)
    # print("######### Topic:", topic)
    return topic


def find_topic_glove(sentence, situation, model, messages):
    dictionary_value = glove.run_glove(sentence, model, messages)
    if dictionary_value == "Threshold issue":
        if situation == "":  # if inserito per fare il test tra i tre
            topic = "low threshold"
        else:
            topic = under_threshold(situation)
    else:
        topic = get_key(dictionary_value)
    # print("######### Topic:", topic)
    return topic


# mettere in keyword_manager
def get_key(val):
    for key, values in kw.keywords_use.items():
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


def under_threshold(situation):
    if len(situation.get_physical_symptoms()) < 4:
        print("Threshold basso, voglio più sintomi fisici")
        return "ask_about_phy_sym"
    if len(situation.get_safety_behaviours()) < 3:
        print("Threshold basso, voglio più comportamenti di difesa")
        return "ask_about_safe_behav"
    print("Threshold basso, ma ho tutto quello che mi serve")
    return "enough"


if __name__ == "__main__":
    main()
