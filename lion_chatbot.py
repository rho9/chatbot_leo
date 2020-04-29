import session_one as s1


def main():
    introduction()


def introduction():
    intro_file = open('data/introduction.txt', "r")
    print(intro_file.read())
    intro_file.close()
    s1.s1_manager()


if __name__ == "__main__":
    main()
