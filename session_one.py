import keys_manager as km
import input_manager as im


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(km.print_question("s1_initial_question"))
    # analyze answer: the user should say something negative,
    # therefore we find keys (work, university, family,..) and we
    # put everything in bad list
    words = im.tokenize(answer)
    bad_list = km.find_keys(words)
    print("bad list: ", bad_list)

