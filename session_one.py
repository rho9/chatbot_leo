import dictionaries_manager as dm
import input_manager as im


def s1_manager():
    intro_s1_file = open('data/intro_session_one', "r")
    print(intro_s1_file.read())
    intro_s1_file.close()
    answer = input(dm.find_question("s1_initial_question"))
    concerns_list = elaborate_concerns(answer)
    print("concerns list: ", concerns_list)
    situations_list = find_situations(concerns_list)
    print("situations: ", situations_list)


def elaborate_concerns(answer):
    concerns_list = dm.find_concerns(answer)
    return concerns_list


def find_situations(concerns_list):
    for concern in concerns_list:
        # now we have to find out how to extrapolate situations keys from sentences
        # we can use regular expression. E.g.: afraid of SOUND * (boring, stupid, ...)
        answer = input(dm.ask_about_concerns(concern))
        key_list = dm.find_situations(answer)
        print("key_list in find_situations: ", key_list)
        print("KEY_LIST[0]: ", key_list[0])
        sen_to_add = answer.split(key_list[0])[1]
        sentence = dm.ask_situations_dictionary(key_list[0])
        print(sentence.replace("*", str(sen_to_add)))

    return ["a", "list"]
