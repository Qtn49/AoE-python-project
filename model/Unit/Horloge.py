from time import sleep

class Horloge():
    seconde = 0
    minute = 0

    def horloge(self):
        while 1:
            sleep(1)
            self.seconde+=1
            if (self.seconde > 59):
                self.seconde = 0
                self.minute+=1
            print(self.minute ,":", self.seconde)

    def horlogex2(self):
        while 1:
            sleep(1/2)
            self.seconde+=1
            if (self.seconde > 59):
                self.seconde = 0
                self.minute+=1
            print(self.minute ,":", self.seconde)





