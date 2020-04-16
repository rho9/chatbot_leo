import kb_manager as kbm
import strings_manager as sm
from concern import Concern


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    concerns = find_concerns()
    concerns = find_situations(concerns)


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


def find_situations(concerns):
    # manage only the first concern
    uncomplete_question = kbm.find_value("situations")
    question = sm.replace_a_star(uncomplete_question, concerns[0].get_concern())
    answer = input(question)
    situations_list = kbm.find_keywords(answer)
    while not situations_list:
        answer = input(kbm.find_value("none"))
        situations_list = kbm.find_keywords(answer)
    concerns[0].add_situations(situations_list)
    return concerns
    # socratic answers
    #replacement = answer.split(keys_list[0])[1]
    #sentence = kbm.find_value(keys_list[0])
    #return sm.replace_a_star(sentence, replacement)
