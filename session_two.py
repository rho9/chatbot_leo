# during this session the chatbot should make a recap about what has been said underlying
# the perception (the number given) that the user has and ask the user if it well understood:
# if it's correct, then go on
# if it's not, find out what is wrong and correct it
# Then the chatbot should suggest to record a video in which the person act like he/she were
# in one of the situation he/she talk about with the chatabot.
# Then the chatbot suggest the user to watch at it focusing on the thing that has ben rated
# Then the chatbot ask the user to rate again the symptoms
# Then the chatbot should compare them with the old one:
# if are rated with a minor number, it points out it to the user and ask him/she what he/she
# thinks about that
# if are similar or more? Search in the document, on the internet...?

import kb_manager as kbm
import strings_manager as sm
FLAG = "fast"


def s2_manager(concerns):
    print("Welcome to session 2!")
    recap(concerns)


def recap(concerns):
    # invece di fare il recap tutto in una frase e chiedere se tutto ok,
    # è meglio suddividerli e chiedere conferma a mano mano
    # proposta: thought with situation, phy sym alone because they are the most
    # important ones for session2 and can be many, saf behav and self focus togheter
    # focusing on self focus
    situations = concerns[0].get_situations()
    situation = situations[0].get_situation()
    ### THOUGHTS ###
    thought = situations[0].get_thoughts()[0]
    thought_rate = situations[0].get_thought_tuples()[0][1]  # [0] first elem of the list; [1] second item of the tuple
    print("You said that when you", situation, "you are", thought, "and that you think that", thought_rate, "out of 10")
    manage_confirmation()
    ### PHYSICAL SYMPTOMS ###
    phy_syms = situations[0].get_physical_symptoms()
    phy_syms_rate = situations[0].get_phy_sym_rates()
    if len(phy_syms) == 1:
        print("You also said that you usually start", phy_syms[0], phy_syms_rate[0], "on a scale of 0 to 10")
    elif len(phy_syms) == 2:
        print("You also said that you usually start", phy_syms[0], phy_syms_rate[0], "and", phy_syms[1], phy_syms_rate[1], "on a scale of 0 to 10")
    else:
        print("To be managed")
        # I don't like the idea of keep going with a list
        # Split in pairs?
        # Ask about only the important ones? (which ones are they?)
    manage_confirmation()


def manage_confirmation():
    print(kbm.find_value("confirmation"))
    answer = input()
    negative = sm.is_negative(answer)
    if negative:
        print("Solve the problem")
