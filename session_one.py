import random
import kb_manager as kbm
import strings_manager as sm
import classifier as cl
from concern import Concern
from situation import Situation
FLAG = "fast"
RATE_NEEDED = True


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    sm.my_print_file(intro_s1_file, FLAG)
    intro_s1_file.close()
    concerns = find_concerns()
    concerns, answer = find_situations(concerns)
    situations = concerns[0].get_situations()
    while True:
        state = call_classifier(answer, situations)
        if state == "enough":
            break
        answer = input()
    # situations = find_reaction(situations, "thoughts")  # managed only one situation
    # situations = find_reaction(situations, "physical_symptoms")
    # situations = find_reaction(situations, "safety_behaviours")
    # situations = find_reaction(situations, "self_focus")
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
        concerns.append(Concern(concern[0]))
    return concerns


# find which are the situations that make the user anxious
def find_situations(concerns):
    # manage only the first concern
    intro_sit_file = open('data/intro_situations.txt', "r")
    sm.my_print_file(intro_sit_file, FLAG)
    intro_sit_file.close()
    # replace * in the questions with the concern it is facing now
    uncompleted_question = cl.choose_sentence("situations")
    question = sm.replace_a_star(uncompleted_question, concerns[0].get_concern())
    sm.my_print_string(question, FLAG)
    answer = input()
    new_answer, keywords_list = analyze_answer(answer)
    for keyword in keywords_list:
        situation = sm.complete_keywords(new_answer, keyword[0])
        concerns[0].add_situation(Situation(situation))
    recap(situation, "sit")
    return concerns, answer
    # socratic answers
    #replacement = answer.split(keys_list[0])[1]
    #sentence = kbm.find_value(keys_list[0])
    #return sm.replace_a_star(sentence, replacement)


# Note: it doesn't make the recap when it finishes the random calls
# NON LO USIAMO PIù
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
            recap(thought, reaction)
    elif reaction == "physical_symptoms":
        for keyword in keywords_list:
            phy_sym = sm.complete_keywords(new_answer, keyword)  # ma serve?
            rate = kbm.find_rate(phy_sym)
            situations[0].add_physical_symptom(phy_sym, rate)
            while new_answer and "no" not in new_answer:
                recap(new_answer, reaction)
                new_answer = ask_more(situations, "phy_sym")
    elif reaction == "safety_behaviours":
        for keyword in keywords_list:
            safe_behav = sm.complete_keywords(new_answer, keyword)
            situations[0].add_safety_behaviour(safe_behav)
            for i in range(random.randrange(1, 3)):
                if new_answer and "no" not in new_answer:
                    recap(new_answer, reaction)
                    new_answer = ask_more(situations, "safe_behav")
    elif reaction == "self_focus":
        for keyword in keywords_list:
            self_focus = sm.complete_keywords(new_answer, keyword)
            situations[0].add_self_focus(self_focus)
            for i in range(random.randrange(1, 3)):
                if new_answer and "no" not in new_answer:
                    recap(new_answer, reaction)
                    new_answer = ask_more(situations, "self_focus")
    elif reaction == "self_image":
        for keyword in keywords_list:
            self_image = sm.complete_keywords(new_answer, keyword)
            situations[0].add_self_image(self_image)
            recap(self_image, reaction)
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
# GNAP MA LO USIAMO ANCORA?!?!
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
def recap(reaction, keyword):
    make_summary = random.randrange(0, 2)  # second number is not included
    if 1:
        recap = cl.choose_sentence("recap")
        if "thoughts1" in keyword:
            reaction = to_second_person(reaction)
            sentence = "you are worried they " + reaction
            recap = sm.replace_a_star(recap, sentence)
        elif "thoughts2" in keyword:
            reaction = to_second_person(reaction)
            sentence = "you are worried to seem " + reaction
            recap = sm.replace_a_star(recap, sentence)
        elif "thoughts3" in keyword:
            reaction = to_second_person(reaction)
            sentence = "you are worried that " + reaction
            recap = sm.replace_a_star(recap, sentence)
        elif "thoughts3" in keyword:
            reaction = to_second_person(reaction)
            recap = sm.replace_a_star(recap, reaction)
        elif "phys1" in keyword:
            reaction = to_second_person(reaction)
            sentence = "you become " + reaction
            recap = sm.replace_a_star(recap, sentence)
        elif "phys2" in keyword:
            reaction = to_second_person(reaction)
            sentence = "you start " + reaction
            recap = sm.replace_a_star(recap, sentence)
        elif "sft1" in keyword or "focus" in keyword or "sit" in keyword:
            reaction = to_second_person(reaction)
            sentence = "you " + reaction
            recap = sm.replace_a_star(recap, sentence)
        elif "sft2" in keyword:
            reaction = to_second_person(reaction)
            sentence = "you " + reaction + " something you have next to you"
            recap = sm.replace_a_star(recap, sentence)
        else:
            print("SIAMO IN UN ALTRO CASO DEL RECAP:", keyword)
        sm.my_print_string(recap, FLAG)
    # Should the answer be composed by different parts?
    # Such as: "okay/I see/..." + "you said that/it sounds like/..."
    # Recap everything is in the list after a "no"?


def to_second_person(reaction):
    reaction = reaction.replace("I ", "you ")
    reaction = reaction.replace(" me", " you")
    reaction = reaction.replace(" my", " your")
    return reaction


def call_classifier(user_sentence, situations):
    keywords_list = kbm.check_for_keywords(user_sentence)
    print("keyword_list:", keywords_list)
    if keywords_list:
        if "thou" in keywords_list[0][1]:
            thought = sm.complete_keywords(user_sentence, keywords_list[0][0])
            rate = kbm.find_rate(thought)
            print("rate:", rate)
            situations[0].add_thought(keywords_list[0][0], rate)
        elif "phys" in keywords_list[0][1]:
            phy_sym = sm.complete_keywords(user_sentence, keywords_list[0][0])
            rate = kbm.find_rate(phy_sym)
            print("rate:", rate)
            situations[0].add_physical_symptom(keywords_list[0][0], rate)
        elif "sft" in keywords_list[0][1]:
            if not keywords_list[0][0] in situations[0].get_safety_behaviours():
                situations[0].add_safety_behaviour(keywords_list[0][0])
        elif "focus" in keywords_list[0][1]:
            if keywords_list[0][0] in situations[0].get_self_focus():
                situations[0].add_self_focus(keywords_list[0][0])  # manca complete_keywords (forse anche da altre parti)
    topic = cl.find_topic_use(user_sentence, situations[0])  # valutare se inserire un tot di frasi per tornare al discorso di prima
    if topic == "enough":
        return topic
    bot_answer = cl.choose_sentence(topic)
    if keywords_list and "sft" in keywords_list[0][1]:  # fare anche per gli altri o toglierlo se lo fa già qualcun altro
        phy_sym_list = situations[0].get_physical_symptoms()
        bot_answer = sm.replace_a_star(bot_answer, phy_sym_list[0])
    # gestire il "non ho capito, puoi ripetere?" perché ora non ti arriva la risposta aggiornata
    if keywords_list:
        reaction_to_save = sm.complete_keywords(user_sentence, keywords_list[0][0])
        recap(reaction_to_save, keywords_list[0][1])
    print(bot_answer)
    return topic
