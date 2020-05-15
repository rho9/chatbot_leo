# A situation is characterised by different reactions
class Situation:
    def __init__(self, situation):
        self.situation = situation
        self.avoided = None
        self.thoughts = []
        self.phy_sym_tuple = []
        self.safety_behaviour = []
        self.self_focus = []
        self.self_image = []

    def get_situation(self):
        return self.situation

    def add_thought(self, thought, rate):
        self.thoughts.append((thought, rate))

    def get_thoughts(self):
        return self.thoughts

    def add_physical_symptom(self, phy_sym, rate):
        self.phy_sym_tuple.append((phy_sym, rate))

    def get_physical_symptoms(self):
        phy_sym_list = []
        for item in self.phy_sym_tuple:
            phy_sym_list.append(item[0])
        return phy_sym_list

    def get_phy_sym_tuples(self):
        return self.phy_sym_tuple

    def add_safety_behaviour(self, safe_behav):
        self.safety_behaviour.append(safe_behav)

    def get_safety_behaviours(self):
        return self.safety_behaviour

    def add_self_focus(self, self_focus):
        self.self_focus.append(self_focus)

    def get_self_focus(self):
        return self.self_focus

    def add_self_image(self, self_image):
        self.self_image.append(self_image)

    def get_self_images(self):
        return self.self_image
