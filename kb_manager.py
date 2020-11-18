import random
import strings_manager as sm
import classifier as cl
from data import knowledge_base as kb
from data import keywords as kw
FLAG = "fast"


# non dovrebbe servire più perché ora si interroga la grammatica invece di questo
# given a key, it returns randomly one of its value
def find_value(key):
    values = kb.dictionary[key]
    return values[random.randint(0, (len(values)-1))]


def get_key(val):
    for key, values in kw.keywords_use.items():
        for value in values:
            if val == value:
                return key
    return "key doesn't exist"


# given a sentence, it finds the keys present in it
def find_keywords(sentence):
    keywords_list = []
    for keyword in kb.keywords:
        if keyword[0] in sentence:
            keywords_list.append(keyword)
    return keywords_list


# given a sentence, it finds the rate present in it
def find_rate(sentence):
    final_rate = None
    for rate in kb.rates:
        if rate in sentence.lower():
            final_rate = rate
            break  # in this way if the user writes 9 out of 10, I save 9
    return final_rate


def ask_for_rate(reaction):  # salvare l'intero così da poter fare il confronto?
    question = cl.choose_sentence("rating")
    if "*" in question:
        question = sm.replace_a_star(question, reaction)
    sm.my_print_string(question, FLAG)
    rate_answer = input()
    rate = find_rate(rate_answer)
    while not rate:
        output = find_value("wrong rating")
        sm.my_print_string(output, FLAG)
        rate_answer = input()
        rate = find_rate(rate_answer)
    return rate


# it finds the typology of the keyword (the number) to know which particle use
def find_typology(keyword):
    typology = None
    for keyword_tuple in kb.keywords:
        if keyword == keyword_tuple[0]:
            typology = keyword_tuple[1]
            break
    return typology


# work in progess for session 2
def update_db(situations, old_thought, new_thought, new_rate):
    # THOUGHTS
    situations[0].change_thought(old_thought, new_thought, new_rate)


# print what has been saved from user's answers
def print_db(concerns, situations):
    print("Concern: ", concerns[0].get_concern())
    print("Situation: ", situations[0].get_situation())
    print("Thought: ", situations[0].get_thought_tuples())
    print("Physical symptoms: ", situations[0].get_phy_sym_tuples())
    print("Safety behaviours: ", situations[0].get_safety_behaviours())
    print("Self focus: ", situations[0].get_self_focus())
