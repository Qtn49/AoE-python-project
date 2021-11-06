from model.Environment import Environment


class GoldMine(Environment):

    def __init__(self, resources=10, image_path=None):
        super().__init__(resources, image_path)

