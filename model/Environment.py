from model.Element import Element


class Environment(Element):

    def __init__(self, x, y, resources=10, appearance=None):
        super().__init__(x, y, appearance)
        self.resources = resources

    def removeSelf(self, player):
        pass
