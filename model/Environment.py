from model.Element import Element


class Environment(Element):

    def __init__(self, x, y, resources=10, image_path=None):
        super().__init__(x, y, image_path)
        self.resources = resources

    def removeSelf(self, player):
        pass