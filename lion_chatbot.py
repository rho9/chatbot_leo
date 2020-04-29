import session_one as s1
import strings_manager as sm
import emotions_manager as em


def main():
    introduction()


def introduction():
    intro_file = open('data/introduction.txt', "r")
    print(intro_file.read())
    intro_file.close()
    s1.s1_manager()


if __name__ == "__main__":
    main()
