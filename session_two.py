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
    # focusing on saf behav
    situations = concerns[0].get_situations()
    situation = situations[0].get_situation()
    ### SITUATION and THOUGHTS ###
    thought = situations[0].get_thoughts()[0]
    thought_rate = situations[0].get_thought_tuples()[0][1]  # [0] first elem of the list; [1] second item of the tuple
    print("You said that when you", situation, "you are", thought, "and that you think that", thought_rate, "out of 10")
    manage_confirmation(situations, "thoughts")
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
    manage_confirmation(situations, "phy_sym")
    ### SAFETY BEHAVIOURS and SELF FOCUS ###
    safe_behavs = situations[0].get_safety_behaviours()
    self_focuss = situations[0].get_self_focus()
    # metterlo in string manager?
    safe_behavs_string = sm.create_string_list(safe_behavs)
    print("Finally, when we talked about safety behaviours and self focus, you said that you tend to", safe_behavs_string)
    print("and you", self_focuss[0])
    manage_confirmation(situations, "safe_bhv_self_focus")
    kbm.print_db(concerns, situations)


def manage_confirmation(situations, reaction):
    print(kbm.find_value("confirmation"))
    answer = input()
    negative = sm.is_negative(answer)
    if negative:
        print("Solve the problem")
        # devi sapere cosa gli hai chiesto per sapere qual è l'elenco da modificare
        # insieme al no potrebbe già esserci la cosa che hai sbagliato e quindi non hai bosogno
        # di chiederglielo
        # altrimenti devi chiederglielo
        # partiamo dal semplice: ti dico una cosa sola e tu mi dici che questa è sbagliata
        # partiamo dal singolo pensiero
        keywords = kbm.check_for_keywords(answer)
        if reaction == "thoughts":
            if not keywords:
                # chiedere cosa è sbagliato
                print("I'm sorry. Can you tell me it again, then?")
                answer = input()
                keywords = kbm.check_for_keywords(answer)
                # per ora ipotizzo che la inserisca correttamente
            # modificare il db
            # aggiungere in situazione "sostituisci" che rimuove e aggiunge
            print("Thought before: ", situations[0].get_thoughts())
            old_thought = situations[0].get_thoughts()[0]  # for now only the first one
            new_thought = sm.complete_keywords(answer, keywords[0])  # [0]: for now we take only the first one
            new_rate = kbm.find_rate(new_thought)  # attenzione: l'utente potrebbe già averlo inserito
            kbm.update_db(situations, old_thought, new_thought, new_rate)
            print("Thought after: ", situations[0].get_thoughts())