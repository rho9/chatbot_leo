import dictionaries_manager as dm
import strings_manager as sm
from concerns_node import Concerns_node


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(dm.find_value("s1_initial_question"))
    concerns = elaborate_concerns(answer)
    situations = find_situations(concerns)
    print(situations)


def elaborate_concerns(answer):
    # we have to add nodes in concerns_node
    concerns_list = dm.find_keys(answer)
    while not concerns_list:
        answer = input(dm.find_value("none"))
        concerns_list = dm.find_keys(answer)
    concerns = []
    for concern in concerns_list:
        concerns.append(Concerns_node(concern))
    return concerns


def find_situations(concerns):
    for concern in concerns:
        answer = input(dm.find_value(concern.get_concern()))
        keys_list = dm.find_keys(answer)
        while not keys_list:
            answer = input(dm.find_value("none"))
            keys_list = dm.find_keys(answer)
        concern.add_list(keys_list)
        # only first situation is managed
        replacement = answer.split(keys_list[0])[1]
        sentence = dm.find_value(keys_list[0])
        return sm.replace_a_star(sentence, replacement)
