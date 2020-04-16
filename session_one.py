import kb_manager as kbm
import strings_manager as sm
from concern import Concern
from situation import Situation


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    concerns = find_concerns()
    concerns = find_not_avoided_situations(concerns)
    situations = concerns[0].get_situations()
    thoughts = find_thoughts()
    situations[0].set_thoughts(thoughts)
    print(situations[0].get_thoughts())


def find_concerns():
    answer = input(kbm.find_value("concerns"))
    concerns_list = kbm.find_keywords(answer)
    while not concerns_list:
        answer = input(kbm.find_value("none"))
        concerns_list = kbm.find_keywords(answer)
    concerns = []
    for concern in concerns_list:
        concerns.append(Concern(concern))
    return concerns


def find_not_avoided_situations(concerns):
    # manage only the first concern
    intro_nas_file = open('data/intro_not_avoided_situations.txt', "r")
    print(intro_nas_file.read())
    intro_nas_file.close()
    uncomplete_question = kbm.find_value("situations")
    print(sm.replace_a_star(uncomplete_question, concerns[0].get_concern()))
    answer = input(kbm.find_value("not_avoided_situations"))
    situations_list = kbm.find_keywords(answer)
    while not situations_list:
        answer = input(kbm.find_value("none"))
        situations_list = kbm.find_keywords(answer)
    for situation in situations_list:
        concerns[0].add_situation(Situation(situation))
    return concerns
    # socratic answers
    #replacement = answer.split(keys_list[0])[1]
    #sentence = kbm.find_value(keys_list[0])
    #return sm.replace_a_star(sentence, replacement)

def find_thoughts():
    return "I've found your thoughts"
