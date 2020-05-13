import random
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
    sm.my_print_string(find_question(situations, reaction, None), FLAG)
    answer = input()
    keywords_list = kbm.check_for_keywords(answer)
    while not keywords_list: # and no not in answer
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
            phy_sym = sm.complete_keywords(answer, keyword)
            rate = find_rate(phy_sym)
            situations[0].add_physical_symptom(phy_sym, rate)
            while "no" not in answer:
                answer = ask_more(situations, "phy_sym")
    elif reaction == "safety_behaviours":
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(answer, keyword)
            situations[0].add_safety_behaviour(safe_behav)
            # i = random.randrange(1, 3)
            for i in range(random.randrange(2, 3)):
                if "no" not in answer:
                    answer = ask_more(situations, "safe_behav")
                # BUG: quando torno qui answer è quella che avevo in questo metodo,
                # non il no che avevo scritto in "ask_more" -> richiede la domanda
    elif reaction == "self_focus":
        for keyword in keywords_list:
            self_focus = sm.complete_keywords(answer, keyword)
            situations[0].add_self_focus(self_focus)
    elif reaction == "self_image":
        for keyword in keywords_list:
            self_image = sm.complete_keywords(answer, keyword)
            situations[0].add_self_image(self_image)
    return situations


def find_question(situations, key, reaction):
    # PROBLEMA. Quando arrivo da ask_more() la reaction (la key di domanda) è la stessa,
    # ma se arrivo dai sintomi devo fare una cosa, se arrivo dai comportamenti un'altra e così via
    # devo aggiungere un campo in più? differenziare key da reaction?
    question = kbm.find_value(key)
    if "*" in question:
        if key == "thoughts" or key == "physical_symptoms":
            question = sm.replace_a_star(question, situations[0].get_situation())
        elif key == "safety_behaviours" or key == "self_focus":
            phys_symp = situations[0].get_physical_symptoms()[0]  # tuple: (physical symptom, rate)
            question = sm.replace_a_star(question, phys_symp[0])
            # it takes the first one. Better random?
        elif key == "more":
            if reaction == "phy_sym":
                index_last_elem = len(situations[0].get_physical_symptoms()) - 1
                phys_symp = situations[0].get_physical_symptoms()[index_last_elem]  # tuple: (physical symptom, rate)
                question = sm.replace_a_star(question, phys_symp[0])
            elif reaction == "safe_behav":
                index_last_elem = len(situations[0].get_safety_behaviours()) - 1
                safe_behav = situations[0].get_safety_behaviours()[index_last_elem]
                question = sm.replace_a_star(question, safe_behav)
    return question


def find_rate(problem):  # salvare l'intero così da poter fare il confronto?
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


# NON DEVI ACCETTARE I DOPPIONI
# alternare questo metodo ad uno con "do you.." + cosa c'è in kb, ma non nella lista?
def ask_more(situations, reaction): # CAMBIA REACTION IN WHAT "FIND_QUESTION" WANTS
    question = find_question(situations, "more", reaction)  # DIVERSO
    sm.my_print_string(question, FLAG)
    answer = input()
    keywords_list = kbm.check_for_keywords(answer)
    while not keywords_list and "no" not in answer:
        sm.my_print_string(kbm.find_value("none"), FLAG)
        answer = input()
        keywords_list = kbm.check_for_keywords(answer)
    if reaction == "phy_sym": # method: ask_until? NO. meglio un metodo solo: il primo lo chiami in loop, il seconfo con l'if
        for keyword in keywords_list:
            phy_sym = sm.complete_keywords(answer, keyword)
            rate = find_rate(phy_sym)  # SOTTO NON C'è
            situations[0].add_physical_symptom(phy_sym, rate)  # DIVERSO
    # passo dal while all'if e cambio lista in cui aggiungo cosa ho trovato..basta..
    elif reaction == "safe_behav":  # method: ask e basta?
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(answer, keyword)
            situations[0].add_safety_behaviour(safe_behav)
    return answer
