import dictionaries_manager as dm
import strings_manager as sm
from data import dictionaries


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(dm.find_value("s1_initial_question"))
    concerns_list = elaborate_concerns(answer)
    print("concerns list: ", concerns_list)
    situations_list = find_situations(concerns_list)
    print("situations: ", situations_list)


def elaborate_concerns(answer):
    concerns_list = dm.find_keys(answer)
    while not concerns_list:
        answer = input(dm.find_value("none"))
        concerns_list = dm.find_keys(answer)
    return concerns_list


def find_situations(concerns_list):
    # when more concerns managed remember to keep in memory all the situations for every concerns
    for concern in concerns_list:
        answer = input(dm.find_value(concern))
        key_list = dm.find_keys(answer)
        while not key_list:
            answer = input(dm.find_value("none"))
            key_list = dm.find_keys(answer)
        print("key_list in find_situations: ", key_list)
        # ora prendo la prima, ma poi dovrò analizzare tutte le chiavi trovate
        print("KEY_LIST[0]: ", key_list[0])
        replacement = str(answer.split(key_list[0])[1])
        print("replacement in find_situaitons:",replacement)
        sentence = dm.find_value(key_list[0])
        return sm.replace_a_star(sentence, replacement)
