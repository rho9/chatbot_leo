# a structure: id node: concern; element of node: list of situations
# questo è solo il nodo. Serve la lista
class Concerns_node:
    def __init__(self, concern):
        self.concern = concern
        self.situations = []

    def add_list(self, situations):
        self.situations = situations

    def get_concern(self):
        return self.concern
