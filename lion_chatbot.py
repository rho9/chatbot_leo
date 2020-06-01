import strings_manager as sm
import kb_manager as kbm
import session_one as s1
import session_two as s2
from concern import Concern
from situation import Situation
FLAG = "fast"


def main():
    introduction()
    #concerns = s1.s1_manager()
    concerns = create_db()
    s2.s2_manager(concerns)


def introduction():
    intro_file = open('data/introduction.txt', "r")
    sm.my_print_file(intro_file, FLAG)
    intro_file.close()


# method created in order to test s2 without answer to s1's questions
def create_db():
    concern = Concern("work")
    concern.add_situation(Situation("have to talk to customers"))
    situation = concern.get_situations()[0]
    situation.add_thought("worried to sound stupid", "9")
    situation.add_physical_symptom("sweating", "8")
    situation.add_safety_behaviour("avoid eye contact")
    situation.add_self_focus("stop being lucid")
    return concern


if __name__ == "__main__":
    main()
