import kb_manager as kbm
import strings_manager as sm
FLAG = "fast"


def s2_manager(concerns):
    print("Now I'd like you to focus on the situation you told me about and how you think you look..")
    recap(concerns)
    video_setup_file = open('data/fixed_texts/first_video_setup.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)
    answer = input()
    video_setup_file = open('data/fixed_texts/second_video_setup.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)
    answer = input()
    video_setup_file = open('data/fixed_texts/watch_videos.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)
    answer = input()
    video_setup_file = open('data/fixed_texts/watch_videos.txt', "r")
    sm.my_print_file(video_setup_file, FLAG)


def recap(concerns):
    situations = concerns[0].get_situations()
    situation = situations[0].get_situation()
    # SITUATION and THOUGHTS
    if situations[0].get_thoughts():
        thought = situations[0].get_thoughts()[0]
        thought_rate = situations[0].get_thought_tuples()[0][1]  # [0] first elem of the list; [1] second item of the tuple
        keyword = kbm.find_typology(thought)
        thought = sm.add_particles(thought, keyword)
        print("You said that when you", situation, thought, "and that you think that", thought_rate, "out of 10")
    # PHYSICAL SYMPTOMS
    phy_syms = situations[0].get_physical_symptoms()
    phy_syms_rate = situations[0].get_phy_sym_rates()
    i = 0
    sentence = "You also said that on a scale of 0 to 10 "
    while i < 4:
        keyword = kbm.find_typology(phy_syms[i])
        phy_sym = sm.add_particles(phy_syms[i], keyword)
        if i != 3:
            sentence = sentence + phy_sym + " " + phy_syms_rate[i] + ", "
        else:
            sentence = sentence + "and " + phy_sym + " " + phy_syms_rate[i]
        i += 1
        # future work: gather characteristic with same rate
    print(sentence)
    # SAFETY BEHAVIOURS and SELF FOCUS
    safe_behavs = situations[0].get_safety_behaviours()
    self_focuss = situations[0].get_self_focus()
    i = 0
    while i < len(safe_behavs):
        keyword = kbm.find_typology(safe_behavs[i])
        safe_behavs[i] = sm.add_particles(safe_behavs[i], keyword)
        i += 1
    safe_behavs_string = sm.create_string_list(safe_behavs)
    print("Finally, when we talked about safety behaviours and self focus, you said that you tend to", safe_behavs_string)
    if self_focuss:
        print("and that you also", self_focuss[0])
