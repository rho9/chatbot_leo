import random
import kb_manager as kbm
import strings_manager as sm
import classifier as cl
from concern import Concern
from situation import Situation
FLAG = "fast"
RATE_NEEDED = True
CHOOSE_TOPIC_METHOD = "use"  # accepted values: counter, glove, use


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
    return concerns, answer


# if the bot doesn't find anything interesting in the user's answer,
# it ask him/her to be more specific
def analyze_answer(answer):
    keywords = kbm.check_for_keywords(answer)
    while not keywords:
        sm.my_print_string(cl.choose_sentence("none"), FLAG)
        answer = input()
        keywords = kbm.check_for_keywords(answer)
    return answer, keywords


# it makes a recap of what the user has just said
def recap(reaction, keyword):
    make_summary = random.randrange(0, 2)  # second number is not included
    if make_summary and keyword != "":
        recap = cl.choose_sentence("recap")
        sentence = sm.add_particles(reaction, keyword)
        recap = sm.replace_a_star(recap, sentence)
        sm.my_print_string(recap, FLAG)


def call_classifier(user_sentence, situations):
    keywords_list = kbm.check_for_keywords(user_sentence)
    situations = update_situation(user_sentence, keywords_list, situations)
    # elaborate an answer
    topic = cl.find_topic(user_sentence, situations[0], CHOOSE_TOPIC_METHOD)
    if topic == "enough":
        return topic
    bot_answer = cl.choose_sentence(topic)
    # replace the star with the right particle
    replacement = ""
    if topic == "safety_behaviours" or topic == "ask_about_safe_behav" or topic == "phys_symp":
        # se ancora non hanno inserito phy sym devi evitare quelle con l'asterisco
        phy_sym_list = situations[0].get_physical_symptoms()
        replacement = sm.add_particles_from_topic(phy_sym_list[0])
    bot_answer = sm.replace_a_star(bot_answer, replacement)
    # gestire il "non ho capito, puoi ripetere?" perché ora non ti arriva la risposta aggiornata
    if keywords_list:
        reaction_to_save = sm.complete_keywords(user_sentence, keywords_list[0][0])
        if topic != "sit":
            recap(reaction_to_save, keywords_list[0][1])
    print(bot_answer)
    return topic


# save new keywords in the first situation
def update_situation(user_sentence, keywords_list, situations):
    if keywords_list:
        if "thou" in keywords_list[0][1]:
            thought = sm.complete_keywords(user_sentence, keywords_list[0][0])
            complete_thought = sm.add_particles(thought,keywords_list[0][1])
            rate = kbm.find_rate(complete_thought)
            situations[0].add_thought(keywords_list[0][0], rate)
        elif "phys" in keywords_list[0][1]:
            phy_sym = sm.complete_keywords(user_sentence, keywords_list[0][0])
            complete_phy_sym = sm.add_particles(phy_sym,keywords_list[0][1])
            rate = kbm.find_rate(complete_phy_sym)
            situations[0].add_physical_symptom(keywords_list[0][0], rate)
        elif "sft" in keywords_list[0][1]:
            if not keywords_list[0][0] in situations[0].get_safety_behaviours():
                situations[0].add_safety_behaviour(keywords_list[0][0])
        elif "focus" in keywords_list[0][1]:
            if not keywords_list[0][0] in situations[0].get_self_focus():
                situations[0].add_self_focus(keywords_list[0][0])  # manca complete_keywords (forse anche da altre parti)
    return situations
