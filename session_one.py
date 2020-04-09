import dictionaries_manager as dm
import input_manager as im


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(dm.find_question("s1_initial_question"))
    concerns_list = elaborate_concerns(answer)
    situations_list = find_situations(concerns_list)
    print("situations: ", situations_list)


def elaborate_concerns(answer):
    words = im.tokenize(answer)
    concerns_list = dm.find_concerns(words)
    return concerns_list


def find_situations(concerns_list):
    for concern in concerns_list:
        print(dm.ask_about_concerns(concern))
        # now we have to find out how to extrapolate situations keys from sentences
        # we can use regular expression. E.g.: afraid of SOUND * (boring, stupid, ...)
    return ["a", "list"]
