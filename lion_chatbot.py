import session_one as s1
import strings_manager as sm
import emotions_manager as em
FLAG = "fast"


def main():
    introduction()


def introduction():
    intro_file = open('data/introduction.txt', "r")
    sm.my_print_file(intro_file, FLAG)
    intro_file.close()
    #s1.s1_manager()
    sen = "Well, for example, when I’m at work I’m really worried about saying something stupid or sounding weird "
    sm.complete_keywords_pos(sen, "worried")


if __name__ == "__main__":
    main()
