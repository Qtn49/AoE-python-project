import threading
import sys

from time import sleep


class Action(threading.Thread):

    def __init__(self, action, args):
        super().__init__()
        self.args = args
        self.action = action
        self.arret = False

    def run(self):
        try:
            self.action(self.args)
            if self.arret:
                raise ValueError("Arrêt de : ", self.action)
        except:
            print(u"%s" % sys.exc_info()[1])

    def stopthread(self):
        self.arret=True