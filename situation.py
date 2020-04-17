# A situation is characterised by different reactions
class Situation:
    def __init__(self, situation):
        self.situation = situation
        self.avoided = None
        self.thoughts = []
        self.physical_sensations = None
        self.safety_behaviour = None
        self.self_focus = None
        self.self_image = None

    def get_situation(self):
        return self.situation

    def add_thought(self, thought):
        self.thoughts.append(thought)

    def get_thoughts(self):
        return self.thoughts
