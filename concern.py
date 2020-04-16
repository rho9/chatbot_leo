class Concern:
    def __init__(self, concern):
        self.concern = concern
        self.situations = []

    def add_situations(self, situations):
        self.situations = situations

    def get_concern(self):
        return self.concern

    def get_situations(self):
        return self.situations
