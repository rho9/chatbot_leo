from datetime import datetime
import strings_manager as sm
import kb_manager as kbm
from data import keywords as kw
from embedding import universal_sentence_encoder_tf as use_tf
from embedding import glove_cosine_similarity as glove


def main():
    sentence = "I don't like when I have to work with other people because it makes me anxious"
    print("Sentence to be analyze:", sentence)
    now = datetime.now()

    # load glove
    glove_model = glove.load_glove_model()
    messages = kbm.update_messages([])

    print("### COUNTER ###")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("Start time =", current_time)
    stems = sm.find_stems(sentence)
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
        stems = sm.find_stems("sentence")
        topic = find_topic_counting_words(stems)
    elif method == "glove":
        glove_model = glove.load_glove_model()
        messages = kbm.update_messages([])
        topic = find_topic_glove(sentence, situation, glove_model, messages)
    elif method == "use":
        topic = find_topic_use(sentence, situation)
    return topic


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


def find_topic_use(sentence, situation):
    messages = kbm.update_messages([])
    dictionary_value = use_tf.run_use(messages, sentence)
    topic = ""
    if dictionary_value == "Threshold issue":
        if situation == "":  # if useful to test the 3 methods
            topic = "low threshold"
        else:
            topic = under_threshold(situation)
    else:
        topic = kbm.get_key(dictionary_value)
    return topic


def find_topic_glove(sentence, situation, model, messages):
    dictionary_value = glove.run_glove(sentence, model, messages)
    if dictionary_value == "Threshold issue":
        if situation == "":  # if useful to test the 3 methods
            topic = "low threshold"
        else:
            topic = under_threshold(situation)
    else:
        topic = kbm.get_key(dictionary_value)
    return topic


def under_threshold(situation):
    if len(situation.get_physical_symptoms()) < 4:
        return "ask_about_phy_sym"
    if len(situation.get_safety_behaviours()) < 3:
        return "ask_about_safe_behav"
    return "enough"


if __name__ == "__main__":
    main()
