#!/usr/bin/env python3

#import sys
#sys.path.insert(1, '/home/gwerle/Documents/INSA/3A/Projet/AoE-class-MAP/')
from Map import *
from Element import *
from time import sleep

#############################
#####     Classes       #####
#############################

class Unit(Element):

    def __init__(self, pos, board):
        super().__init__(pos, board)


    def disp_position(self, board):
        unit = board.getElement((self.pos[0],self.pos[1]))
        print("{}:{}".format(self.pos[0],self.pos[1]))

    def move(self, new_pos, board):

        dir=0
        notH = False
        notV = False

        while self.pos!=new_pos:

            if self.pos[0] < new_pos[0]:
                dirH = 1
            elif self.pos[0] > new_pos[0]:
                dirH = -1
            else :
                dirH = 0

            if self.pos[1] < new_pos[1]:
                dirV = 1
            elif self.pos[1] > new_pos[1]:
                dirV = -1
            else :
                dirV = 0

            if (dir==0 or notV):
                #horizontal
                x=self.pos[0]+dirH
                y=self.pos[1]

                if (x,y)!=self.pos:
                    notV = False
                if (x,y) in board.elements:
                    notH=True
                    x=self.pos[0]

            elif (dir==1 or notH):
                #vertical
                x=self.pos[0]
                y=self.pos[1]+dirV

                if (x,y)!=self.pos:
                    notH = False
                if (x,y) in board.elements:
                    notV=True
                    y=self.pos[1]

            print("{} : {}".format(notV,notH))
            if notV and notH:
                print("Bloqué/20")
                break


            board.removeElement(self.pos)

            self.pos=(x,y)

            board.addElement(self.pos, self)

            dir = 1-dir
            sleep(self.spd/100)
            self.scan(board)
            self.disp_position(board)


class Villager(Unit):
    pvBase=25
    atk=3
    atk_spd = 50
    range = 0
    sight = 4
    spd = 50

    def __init__(self, team, pos, board):
        self.pv = self.pvBase
        self.team = team
        super().__init__(pos, board)

    def attack(self, board):
        pass

    def scan(self, board):

        for i in range(-self.sight, self.sight+1):
            x=self.pos[0]+i

            for j in range(-self.sight, self.sight+1):
                y=self.pos[1]+j

                if (x>=0 and y>=0) and (abs(j)+abs(i)<=self.sight) and (x,y)!=self.pos:
                    #print("scan {}:{}".format(x,y))
                    if (x,y) in board.elements:
                        print("{} : vu sur {}:{}".format(self.team, x,y))
                        objet = board.elements[(x,y)]

                        if objet.team!=self.team and objet.team != None:
                            print("hostile")


##############################
#####   Programme       ######
##############################

board = Map()
vilR = Villager("Rouge",(0,0),board)
vilB = Villager("Bleu", (5,8), board)
print(type(Villager.sight))
vilR.disp_position(board)
vilR.move((5,8), board)
