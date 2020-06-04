# A situation is characterised by different reactions
class Situation:
    def __init__(self, situation):
        self.situation = situation
        self.avoided = None
        self.thought_tuple_list = []
        self.phy_sym_tuple_list = []
        self.safety_behaviour = []
        self.self_focus = []
        self.self_image = []

    def get_situation(self):
        return self.situation

    def add_thought(self, thought, rate):
        self.thought_tuple_list.append((thought, rate))

    def get_thoughts(self):
        thoughts_list = []
        for item in self.thought_tuple_list:
            thoughts_list.append(item[0])
        return thoughts_list

    def get_thought_tuples(self):
        return self.thought_tuple_list

    def add_physical_symptom(self, phy_sym, rate):
        self.phy_sym_tuple_list.append((phy_sym, rate))

    def get_physical_symptoms(self):
        phy_sym_list = []
        for item in self.phy_sym_tuple_list:
            phy_sym_list.append(item[0])
        return phy_sym_list

    def get_phy_sym_rates(self):
        phy_sym_rates = []
        for item in self.phy_sym_tuple_list:
            phy_sym_rates.append(item[1])
        return phy_sym_rates

    def get_phy_sym_tuples(self):
        return self.phy_sym_tuple_list

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
