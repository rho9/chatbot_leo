import strings_manager as im
import session_one as s1

def main():
    introduction()


def introduction():
    intro_file = open('data/introduction.txt', "r")
    print(intro_file.read())
    intro_file.close()
    # question = input("\nDo you have any questions? ")
    # not only yes, but synonyms
    # print("ok, I answer") if "yes" in question else print("ok, let's go on")
    # im.tokenize(question)
    s1.s1_manager()


if __name__ == "__main__":
    main()
