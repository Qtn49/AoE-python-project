import abc


class Element:

    def __init__(self, x, y, image_path=None):
        self.image_path = image_path
        self.x = x
        self.y = y
        self.present = True

    @abc.abstractmethod
    def removeSelf(self, player):
        pass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image_path(self):
        return self.image_path
