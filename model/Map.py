from model.Element import Element


class Map:

    def __init__(self, background=None):
        self.elements = []
        self.background = background

    def addElement(self, element):
        self.elements.append(element)

    def removeElement(self, element):
        self.elements.remove(element)

    # TODO define this method with the PyGame Library
    # @property
    # def createInterface(self, draw):
