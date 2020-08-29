import random
import kb_manager as kbm
import strings_manager as sm
import classifier as cl
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
    print("DB from while we are in session one:")
    kbm.print_db(concerns, situations)
    return concerns


# find what concerns the user according to its answer
def find_concerns():
    sm.my_print_string(cl.choose_sentence("concerns"), FLAG)
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
    uncompleted_question = cl.choose_sentence("situations")
    question = sm.replace_a_star(uncompleted_question, concerns[0].get_concern())
    sm.my_print_string(question, FLAG)
    # sm.my_print_string(kbm.find_value("not_avoided_situations"), FLAG)
    # commentata perché le domande sono state inglobata nella grammatica di situations
    answer = input()
    new_answer, keywords_list = analyze_answer(answer)
    for keyword in keywords_list:
        situation = sm.complete_keywords(new_answer, keyword)
        concerns[0].add_situation(Situation(situation))
    recap(situation)
    return concerns
    # socratic answers
    #replacement = answer.split(keys_list[0])[1]
    #sentence = kbm.find_value(keys_list[0])
    #return sm.replace_a_star(sentence, replacement)


# Note: it doesn't make the recap when it finishes the random calls
def find_reaction(situations, reaction):
    # better: first part in a method + sequential execution without elif
    sm.my_print_string(find_question(situations, reaction, None), FLAG)
    answer = input()
    new_answer, keywords_list = analyze_answer(answer)
    if reaction == "thoughts":
        for keyword in keywords_list:
            thought = sm.complete_keywords(new_answer, keyword)
            rate = kbm.find_rate(thought)
            situations[0].add_thought(thought, rate)
            recap(thought)
    elif reaction == "physical_symptoms":
        for keyword in keywords_list:
            phy_sym = sm.complete_keywords(new_answer, keyword)  # ma serve?
            rate = kbm.find_rate(phy_sym)
            situations[0].add_physical_symptom(phy_sym, rate)
            while new_answer and "no" not in new_answer:
                recap(new_answer)
                new_answer = ask_more(situations, "phy_sym")
    elif reaction == "safety_behaviours":
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(new_answer, keyword)
            situations[0].add_safety_behaviour(safe_behav)
            for i in range(random.randrange(1, 3)):
                if new_answer and "no" not in new_answer:
                    recap(new_answer)
                    new_answer = ask_more(situations, "safe_behav")
    elif reaction == "self_focus":
        for keyword in keywords_list:
            self_focus = sm.complete_keywords(new_answer, keyword)
            situations[0].add_self_focus(self_focus)
            for i in range(random.randrange(1, 3)):
                if new_answer and "no" not in new_answer:
                    recap(new_answer)
                    new_answer = ask_more(situations, "self_focus")
    elif reaction == "self_image":
        for keyword in keywords_list:
            self_image = sm.complete_keywords(new_answer, keyword)
            situations[0].add_self_image(self_image)
            recap(self_image)
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
            rate = kbm.find_rate(phy_sym)
            situations[0].add_physical_symptom(phy_sym, rate)
    elif reaction == "safe_behav":
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(answer, keyword)
            # if the safe behaviour is already in the list,
            # it goes to the next question without saving it
            if safe_behav in situations[0].get_safety_behaviours():
                print("You already said it. Let's move on")
                return None
            situations[0].add_safety_behaviour(safe_behav)
    elif reaction == "self_focus":
        for keyword in keywords_list:
            self_focus = sm.complete_keywords(answer, keyword)
            # if the self-focus is already in the list,
            # it goes to the next question without saving it
            if self_focus in situations[0].get_self_focus():
                print("You already said it. Let's move on")
                return None
            situations[0].add_self_focus(self_focus)
    return answer


# it makes a recap of what the user has just said
# NOTE: you must link in a better way what is in reaction and the dictionary value
# HOW? Like were in the Yoda exercise?
def recap(reaction):
    make_summary = random.randrange(0, 2)  # second number is not included
    # print("make_summary: ", make_summary)
    if make_summary == 1:
        recap = kbm.find_value("recap")
        recap = sm.replace_a_star(recap, reaction)
        sm.my_print_string(recap, FLAG)
    # Should the answer be composed by different parts?
    # Such as: "okay/I see/..." + "you said that/it sounds like/..."
    # Recap everything is in the list after a "no"?
