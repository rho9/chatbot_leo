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
    situations = find_reaction(situations, "thoughts")  # managed only one situation
    situations = find_reaction(situations, "physical_symptoms")
    situations = find_reaction(situations, "safety_behaviours")
    situations = find_reaction(situations, "self_focus")
    # situations = find_reaction(situations, "self_image")


def find_concerns():
    answer = input(kbm.find_value("concerns"))
    concerns_list = kbm.check_for_keywords(answer)
    while not concerns_list:
        answer = input(kbm.find_value("none"))
        concerns_list = kbm.check_for_keywords(answer)
    concerns = []
    for concern in concerns_list:
        concerns.append(Concern(concern))
    return concerns


def find_not_avoided_situations(concerns):
    # manage only the first concern
    intro_nas_file = open('data/intro_not_avoided_situations.txt', "r")
    print(intro_nas_file.read())
    intro_nas_file.close()
    uncompleted_question = kbm.find_value("situations")
    print(sm.replace_a_star(uncompleted_question, concerns[0].get_concern()))
    answer = input(kbm.find_value("not_avoided_situations"))
    keywords_list = kbm.check_for_keywords(answer)
    while not keywords_list:
        answer = input(kbm.find_value("none"))
        keywords_list = kbm.check_for_keywords(answer)
    print("keywords_list: ", keywords_list)
    for keyword in keywords_list:
        situation = sm.complete_keywords(answer, keyword)
        concerns[0].add_situation(Situation(situation))
    return concerns
    # socratic answers
    #replacement = answer.split(keys_list[0])[1]
    #sentence = kbm.find_value(keys_list[0])
    #return sm.replace_a_star(sentence, replacement)


def find_reaction(situations, reaction):
    # better: first part in a method + sequential execution without elif
    answer = input(find_question(situations, reaction))
    keywords_list = kbm.check_for_keywords(answer)
    while not keywords_list:
        answer = input(kbm.find_value("none"))
        keywords_list = kbm.check_for_keywords(answer)
    if reaction == "thoughts":
        for keyword in keywords_list:
            thought = sm.complete_keywords(answer, keyword)
            rate = find_rate(thought)
            situations[0].add_thought(thought, rate)
    elif reaction == "physical_symptoms":
        for keyword in keywords_list:
            phy_sym = sm.complete_keywords(answer, keyword)
            rate = find_rate(phy_sym)
            situations[0].add_physical_symptom(phy_sym, rate)
    elif reaction == "safety_behaviours":
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(answer, keyword)
            situations[0].add_safety_behaviour(safe_behav)
    elif reaction == "self_focus":
        for keyword in keywords_list:
            self_focus = sm.complete_keywords(answer, keyword)
            situations[0].add_self_focus(self_focus)
    elif reaction == "self_image":
        for keyword in keywords_list:
            self_image = sm.complete_keywords(answer, keyword)
            situations[0].add_self_image(self_image)
    return situations


def find_question(situations, reaction):
    question = kbm.find_value(reaction)
    if "*" in question:
        if reaction == "thoughts" or reaction == "physical_symptoms":
            question = sm.replace_a_star(question, situations[0].get_situation())
        elif reaction == "safety_behaviours" or reaction == "self_focus":
            phys_symp = situations[0].get_physical_symptoms()[0]  # tuple: (physical symptom, rate)
            question = sm.replace_a_star(question, phys_symp[0])
            # it takes the first one. Better random?
    return question


def find_rate(problem):
    question = kbm.find_value("rating")
    if "*" in question:
        question = sm.replace_a_star(question, problem)
    rate_answer = input(question)
    rate = kbm.check_for_rate(rate_answer)
    while not rate:
        rate_answer = input(kbm.find_value("wrong rating"))
        rate = kbm.check_for_rate(rate_answer)
    return rate
