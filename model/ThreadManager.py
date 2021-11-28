import threading
import sys


class Threadatuer(threading.Thread):
    """
    Sous-classe de threading.Thread, avec une methode tuer()
    """

    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.atuer = False

    def start(self):
        self.run_sav = self.run
        self.run = self.run2
        threading.Thread.start(self)

    def run2(self):
        sys.settrace(self.trace)
        self.run_sav()
        self.run = self.run_sav

    def trace(self, frame, event, arg):
        if self.atuer:
            if event == 'line':
                raise SystemExit()
        return self.trace

    def tuer(self):
        self.atuer = True