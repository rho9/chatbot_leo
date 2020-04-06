import dictionaries_manager as km
import input_manager as im


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(km.print_question("s1_initial_question"))
    words = im.tokenize(answer)
    concerns_list = km.find_keys(words)
    print("bad list: ", concerns_list)
    # we need situations examples for each element in the concern list
    # -> ask in different ways to give them for the first, the second..ect
    # create a dictionary for situations and write as keys the most commons. Put in a list
    # tha one of the patient and answer with what is in the values

