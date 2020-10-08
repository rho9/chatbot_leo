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
import session_one as s1  # add_particle è da spostare in un posto pù consono
import strings_manager as sm
FLAG = "fast"


def s2_manager(concerns):
    print("Now I'd like you to focus on the situation you told me about and how you think you look..")
    recap(concerns)
    video_setup_file = open('data/first_video_setup.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)
    answer = input()
    video_setup_file = open('data/second_video_setup.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)
    answer = input()
    video_setup_file = open('data/watch_videos.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)
    answer = input()
    video_setup_file = open('data/watch_videos.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)


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
    keyword = kbm.find_typology(thought)
    thought = s1.add_particles(thought, keyword)
    print("You said that when you", situation, thought, "and that you think that", thought_rate, "out of 10")
    # manage_confirmation(situations, "thoughts")
    ### PHYSICAL SYMPTOMS ###
    phy_syms = situations[0].get_physical_symptoms()
    phy_syms_rate = situations[0].get_phy_sym_rates()
    i = 0
    sentence = "You also said that on a scale of 0 to 10 "
    while i < 4:
        keyword = kbm.find_typology(phy_syms[i])
        phy_sym = s1.add_particles(phy_syms[i], keyword)
        if i != 3:
            sentence = sentence + phy_sym + " " + phy_syms_rate[i] + ", "
        else:
            sentence = sentence + "and " + phy_sym + " " + phy_syms_rate[i]
        i += 1
        #sappiamo che saranno quattro. quelli con lo stesso rate li mettiamo insieme
        # gli altri facciamo no. in futuro. ora non c'è tempo
    print(sentence)
    # manage_confirmation(situations, "phy_sym")
    ### SAFETY BEHAVIOURS and SELF FOCUS ###
    safe_behavs = situations[0].get_safety_behaviours()
    self_focuss = situations[0].get_self_focus()
    # metterlo in string manager?
    i = 0
    while i < len(safe_behavs):
        keyword = kbm.find_typology(safe_behavs[i])
        safe_behavs[i] = s1.add_particles(safe_behavs[i], keyword)
        i += 1
    safe_behavs_string = sm.create_string_list(safe_behavs)
    print("Finally, when we talked about safety behaviours and self focus, you said that you tend to", safe_behavs_string)
    print("and that you also", self_focuss[0])
    # manage_confirmation(situations, "safe_bhv_self_focus")
    kbm.print_db(concerns, situations)

# not used
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
        keywords = kbm.check_for_keywords(answer)  # non stai gestendo il rating
        if reaction == "thoughts":
            if not keywords:
                # chiedere cosa è sbagliato
                print(kbm.find_value("confirmation"))
                answer = input()
                keywords = kbm.check_for_keywords(answer)
                # per ora ipotizzo che la inserisca correttamente
            old_thought = situations[0].get_thoughts()[0]  # for now only the first one
            new_thought = sm.complete_keywords(answer, keywords[0])  # [0]: for now we take only the first one
            new_rate = kbm.find_rate(new_thought)  # attenzione: l'utente potrebbe già averlo inserito
            kbm.update_db(situations, old_thought, new_thought, new_rate)
        if reaction == "phy_sym":
            # se l'errore è nei physical symptoms gli fai la solita la domanda
            # lui dirà: non è x, ma y -> ok, stesso rate?
            # oppure: non è questo rate, ma questo
            print(kbm.find_value("confirmation"))

