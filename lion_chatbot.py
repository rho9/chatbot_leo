import session_one as s1
import strings_manager as sm
FLAG = "fast"


def main():
    introduction()
    s1.s1_manager()


def introduction():
    intro_file = open('data/introduction.txt', "r")
    sm.my_print_file(intro_file, FLAG)
    intro_file.close()


if __name__ == "__main__":
    main()
