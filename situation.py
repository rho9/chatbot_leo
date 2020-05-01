# A situation is characterised by different reactions
class Situation:
    def __init__(self, situation):
        self.situation = situation
        self.avoided = None
        self.thoughts = []
        self.physical_symptoms = []
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
        self.physical_symptoms.append((phy_sym, rate))

    def get_physical_symptoms(self):
        return self.physical_symptoms

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
