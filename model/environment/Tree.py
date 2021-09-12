from model.Environment import Environment


class Tree(Environment):

    def __init__(self, x, y, resources=10, appearance=None):
        super().__init__(resources, x, y, appearance)

