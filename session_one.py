import dictionaries_manager as dm
import input_manager as im


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(dm.find_question("s1_initial_question"))
    words = im.tokenize(answer)
    concerns_list = dm.find_concerns(words)
    # we need situations examples for each element in the concern list
    # -> ask in different ways to give them for the first, the second..ect
    # create a dictionary for situations and write as keys the most commons. Put in a list
    # tha one of the patient and answer with what is in the values
    find_situations(concerns_list)

def find_situations(concerns_list):
    for concern in concerns_list:
        print("Why don't you talk me about your problem at work?")
