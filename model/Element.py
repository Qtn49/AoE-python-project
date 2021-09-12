import abc


class Element:

    def __init__(self, x, y, appearance=None):
        self.appearance = appearance
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

    def get_appearance(self):
        return self.appearance
