import dictionaries_manager as dm
import strings_manager as sm
from data import dictionaries


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(dm.ask_questions_dictionary("s1_initial_question"))
    concerns_list = elaborate_concerns(answer)
    print("concerns list: ", concerns_list)
    situations_list = find_situations(concerns_list)
    print("situations: ", situations_list)


def elaborate_concerns(answer):
    concerns_list = dm.find_keys(answer, dictionaries.concerns_dictionary)
    return concerns_list


def find_situations(concerns_list):
    for concern in concerns_list:
        answer = input(dm.ask_concerns_dictionary(concern))
        key_list = dm.find_keys(answer, dictionaries.situations_dictionary)
        print("key_list in find_situations: ", key_list)
        # ora prendo la prima, ma poi dovrò analizzare tutte le chiavi trovate
        print("KEY_LIST[0]: ", key_list[0])
        replacement = str(answer.split(key_list[0])[1])
        sentence = dm.ask_situations_dictionary(key_list[0])
        return sm.replace_a_star(sentence, key)
