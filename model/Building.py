from model.Element import Element


class Building(Element):

    def __init__(self, x, y, appearance=None):
        super().__init__(x, y, appearance)
