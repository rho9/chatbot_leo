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

    def add_thought(self, thought):
        self.thoughts.append(thought)

    def get_thoughts(self):
        return self.thoughts

    def add_physical_symptom(self, phy_sym):
        self.physical_symptoms.append(phy_sym)

    def get_physical_symptoms(self):
        return self.physical_symptoms

    def add_safety_behaviour(self, safe_behav):
        self.safety_behaviour.append(safe_behav)

    def add_self_focus(self, self_focus):
        self.self_focus.append(self_focus)

    def add_self_image(self, self_image):
        self.self_image.append(self_image)
