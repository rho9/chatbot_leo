import input_manager


def main():
    introduction()


def introduction():
    intro_file = open('data/introduction.txt', "r")
    print(intro_file.read())
    intro_file.close()
    question = input("\nDo you have any questions? ")
    # not only yes, but synonyms
    print("ok, I answer") if "yes" in question else print("ok, let's go on")

    input_manager.tokenize(question)


def first_session():
    return 0


if __name__ == "__main__":
    main()
