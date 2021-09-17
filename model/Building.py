from model.Element import Element


class Building(Element):

    def __init__(self, x, y, image_path=None):
        super().__init__(x, y, image_path)
