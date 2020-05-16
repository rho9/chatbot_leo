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
    print_db(concerns, situations)


# print what has been saved from user's answers
def print_db(concerns, situations):
    print("Concern: ", concerns[0].get_concern())
    print("Situation: ", situations[0].get_situation())
    print("Thought: ", situations[0].get_thought_tuples())
    print("Physical symptoms: ", situations[0].get_phy_sym_tuples())
    print("Safety behaviours: ", situations[0].get_safety_behaviours())
    print("Self focus: ", situations[0].get_self_focus())


# find what concerns the user according to its answer
def find_concerns():
    sm.my_print_string(kbm.find_value("concerns"), FLAG)
    answer = input()
    new_answer, concerns_list = analyze_answer(answer)
    concerns = []
    for concern in concerns_list:
        concerns.append(Concern(concern))
    return concerns


# find which are the situations in which the user can remain
def find_not_avoided_situations(concerns):
    # manage only the first concern
    intro_nas_file = open('data/intro_not_avoided_situations.txt', "r")
    sm.my_print_file(intro_nas_file, FLAG)
    intro_nas_file.close()
    # replace * in the questions with the concern it is facing now
    uncompleted_question = kbm.find_value("situations")
    question = sm.replace_a_star(uncompleted_question, concerns[0].get_concern())
    sm.my_print_string(question, FLAG)
    sm.my_print_string(kbm.find_value("not_avoided_situations"), FLAG)
    answer = input()
    new_answer, keywords_list = analyze_answer(answer)
    for keyword in keywords_list:
        situation = sm.complete_keywords(new_answer, keyword)
        concerns[0].add_situation(Situation(situation))
    recap()
    return concerns
    # socratic answers
    #replacement = answer.split(keys_list[0])[1]
    #sentence = kbm.find_value(keys_list[0])
    #return sm.replace_a_star(sentence, replacement)


def find_reaction(situations, reaction):
    # better: first part in a method + sequential execution without elif
    sm.my_print_string(find_question(situations, reaction, None), FLAG)
    answer = input()
    new_answer, keywords_list = analyze_answer(answer)
    if reaction == "thoughts":
        for keyword in keywords_list:
            thought = sm.complete_keywords(new_answer, keyword)
            rate = find_rate(thought)
            situations[0].add_thought(thought, rate)
    elif reaction == "physical_symptoms":
        for keyword in keywords_list:
            phy_sym = sm.complete_keywords(new_answer, keyword)  # ma serve?
            rate = find_rate(phy_sym)
            situations[0].add_physical_symptom(phy_sym, rate)
            while new_answer and "no" not in new_answer:
                recap()
                new_answer = ask_more(situations, "phy_sym")
    elif reaction == "safety_behaviours":
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(new_answer, keyword)
            situations[0].add_safety_behaviour(safe_behav)
            for i in range(random.randrange(1, 3)):
                if new_answer and "no" not in new_answer:
                    recap()
                    new_answer = ask_more(situations, "safe_behav")
    elif reaction == "self_focus":
        for keyword in keywords_list:
            self_focus = sm.complete_keywords(new_answer, keyword)
            situations[0].add_self_focus(self_focus)
    elif reaction == "self_image":
        for keyword in keywords_list:
            self_image = sm.complete_keywords(new_answer, keyword)
            situations[0].add_self_image(self_image)
    recap()
    return situations


def find_question(situations, key, reaction):
    question = kbm.find_value(key)
    if "*" in question:
        if key == "thoughts" or key == "physical_symptoms":
            question = sm.replace_a_star(question, situations[0].get_situation())
        elif key == "safety_behaviours" or key == "self_focus":
            phy_sym_list = situations[0].get_physical_symptoms()
            question = sm.replace_a_star(question, phy_sym_list[0])
            # it takes the first one. Better random?
        elif key == "more":
            if reaction == "phy_sym":
                index_last_elem = len(situations[0].get_physical_symptoms()) - 1
                phy_sym_list = situations[0].get_physical_symptoms()[index_last_elem]
                question = sm.replace_a_star(question, phy_sym_list)
            elif reaction == "safe_behav":
                index_last_elem = len(situations[0].get_safety_behaviours()) - 1
                safe_behav = situations[0].get_safety_behaviours()[index_last_elem]
                question = sm.replace_a_star(question, safe_behav)
    return question


def find_rate(reaction):  # salvare l'intero così da poter fare il confronto?
    question = kbm.find_value("rating")
    if "*" in question:
        question = sm.replace_a_star(question, reaction)
    sm.my_print_string(question, FLAG)
    rate_answer = input()
    rate = kbm.check_for_rate(rate_answer)
    while not rate:
        output = kbm.find_value("wrong rating")
        sm.my_print_string(output, FLAG)
        rate_answer = input()
        rate = kbm.check_for_rate(rate_answer)
    return rate


# if the bot doesn't find anything interesting in the user's answer,
# it ask him/her to be more specific
def analyze_answer(answer):
    keywords = kbm.check_for_keywords(answer)
    while not keywords:
        sm.my_print_string(kbm.find_value("none"), FLAG)
        answer = input()
        keywords = kbm.check_for_keywords(answer)
    return answer, keywords


# alternare questo metodo ad uno con "do you.." + cosa c'è in kb, ma non nella lista?
def ask_more(situations, reaction):
    question = find_question(situations, "more", reaction)
    sm.my_print_string(question, FLAG)
    answer = input()
    keywords_list = kbm.check_for_keywords(answer)
    while not keywords_list and "no" not in answer:
        sm.my_print_string(kbm.find_value("none"), FLAG)
        answer = input()
        keywords_list = kbm.check_for_keywords(answer)
    if reaction == "phy_sym":
        for keyword in keywords_list:
            phy_sym = sm.complete_keywords(answer, keyword)
            # if the physical symptom is already in the list,
            # it goes to the next question without saving the physical symptom
            if phy_sym in situations[0].get_physical_symptoms():
                print("You already said it. Let's move on")
                return None
            rate = find_rate(phy_sym)
            situations[0].add_physical_symptom(phy_sym, rate)
    elif reaction == "safe_behav":
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(answer, keyword)
            # if the safe behaviour is already in the list,
            # it goes to the next question without saving the safe behaviour
            if safe_behav in situations[0].get_safety_behaviours():
                print("You already said it. Let's move on")
                return None
            situations[0].add_safety_behaviour(safe_behav)
    #recap()
    return answer


# creo un metodo per ripetere cosa ha detto l'utente prima di fare la domanda
# decidere:
# - da chi viene chiamato
# - il nome
# - se farlo tutte le volte (mi sembra troppo) o random
# - se serve creare una chiave nel dizionario
# - cosa fa
# - se creare la risposta con più parti: okay/I see/... + hai detto che
def recap():
    make_summary = 1  #random.randrange(0, 1)
    if make_summary == 1:
        print("Dico qualcosa che hai appena detto tu")
    else:
        print("Non dico niente e faccio come al solito")
