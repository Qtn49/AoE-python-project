from model.Environment import Environment


class GoldMine(Environment):

    def __init__(self, x, y, resources=10, appearance=None):
        super().__init__(resources, x, y, appearance)

