import kb_manager as kbm
import strings_manager as sm
from concern import Concern
from situation import Situation
FLAG = "fast"


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    sm.my_print_file(intro_s1_file, FLAG)
    intro_s1_file.close()
    concerns = find_concerns()
    concerns = find_not_avoided_situations(concerns)
    situations = concerns[0].get_situations()
    situations = find_reaction(situations, "thoughts")  # managed only one situation
    situations = find_reaction(situations, "physical_symptoms")
    situations = find_reaction(situations, "safety_behaviours")
    situations = find_reaction(situations, "self_focus")
    # situations = find_reaction(situations, "self_image")
    print("Concern: ", concerns[0].get_concern())
    print("Situation: ", situations[0].get_situation())
    print("Thought: ", situations[0].get_thoughts())
    print("Physical symptoms: ", situations[0].get_physical_symptoms())
    print("Safety behaviours: ", situations[0].get_safety_behaviours())
    print("Self focus: ", situations[0].get_self_focus())


def find_concerns():
    sm.my_print_string(kbm.find_value("concerns"), FLAG)
    answer = input()
    concerns_list = kbm.check_for_keywords(answer)
    while not concerns_list:
        sm.my_print_string(kbm.find_value("none"), FLAG)
        answer = input()
        concerns_list = kbm.check_for_keywords(answer)
    concerns = []
    for concern in concerns_list:
        concerns.append(Concern(concern))
    return concerns


def find_not_avoided_situations(concerns):
    # manage only the first concern
    intro_nas_file = open('data/intro_not_avoided_situations.txt', "r")
    sm.my_print_file(intro_nas_file, FLAG)
    intro_nas_file.close()
    uncompleted_question = kbm.find_value("situations")
    question = sm.replace_a_star(uncompleted_question, concerns[0].get_concern())
    sm.my_print_string(question, FLAG)
    sm.my_print_string(kbm.find_value("not_avoided_situations"), FLAG)
    answer = input()
    keywords_list = kbm.check_for_keywords(answer)
    while not keywords_list:
        sm.my_print_string(kbm.find_value("none"), FLAG)
        answer = input()
        keywords_list = kbm.check_for_keywords(answer)
    #print("keywords_list: ", keywords_list)
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
    sm.my_print_string(find_question(situations, reaction), FLAG)
    answer = input()
    keywords_list = kbm.check_for_keywords(answer)
    while not keywords_list:
        sm.my_print_string(kbm.find_value("none"), FLAG)
        answer = input()
        keywords_list = kbm.check_for_keywords(answer)
    if reaction == "thoughts":
        for keyword in keywords_list:
            thought = sm.complete_keywords(answer, keyword)
            rate = find_rate(thought)
            situations[0].add_thought(thought, rate)
    elif reaction == "physical_symptoms":
        for keyword in keywords_list:
            #ora faccio una domanda sola
            # io ho bisogno di farne di più
            # per ora pensa solo a questo, poi vediamo come espanderci
            # un loop finchè non mi dice basta?
            # un numero random tra 1 e n?
            # andrei con il basta
            # userei una nuova entry nel dizionario "ask_more"
            # ogni volta devi aggiungere alla lista latrimenti non puoi usare cosa ti ha appena detto
            # nelle domande dopo
            # usare una "do you.." + cosa c'è in kb, ma non nella lista?
            phy_sym = sm.complete_keywords(answer, keyword)
            print("gnap0")
            rate = find_rate(phy_sym)
            print("ganp1")
            situations[0].add_physical_symptom(phy_sym, rate)
            # ask for more physical symptoms
            while True:
                sm.my_print_string(find_question(situations, "ask_for_more_ph_sym"), FLAG)
                answer = input()
                if "no" in answer:
                    print("I found no")
                    break
                keywords_list = kbm.check_for_keywords(answer)
                for keyword in keywords_list:
                    print("I keep going on")
                    phy_sym = sm.complete_keywords(answer, keyword)
                    rate = find_rate(phy_sym)
                    situations[0].add_physical_symptom(phy_sym, rate)
            # prendo un valore a caso da kbm.find_value
            # faccio la domanda
            # prendo la risposta
            # è un no -> esco dal while
            # altrimetni la inserisco nella giusta lista di situation
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
    sm.my_print_string(question, FLAG)
    rate_answer = input()
    rate = kbm.check_for_rate(rate_answer)
    while not rate:
        output = kbm.find_value("wrong rating")
        sm.my_print_string(output, FLAG)
        rate_answer = input()
        rate = kbm.check_for_rate(rate_answer)
    return rate
