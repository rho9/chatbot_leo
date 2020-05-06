import session_one as s1
import strings_manager as sm
import emotions_manager as em
FLAG = "fast"


def main():
    introduction()


def introduction():
    intro_file = open('data/introduction.txt', "r")
    sm.my_print(intro_file, FLAG)
    intro_file.close()
    s1.s1_manager()


if __name__ == "__main__":
    main()
