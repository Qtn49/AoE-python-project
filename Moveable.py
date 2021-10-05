#!/usr/bin/env python3

from Map import *
from Element import *
from time import sleep


class Moveable(Element):

    units =[{'pv':25,'atk':3,'atk_spd':50,'rng':1,'sight':4,'spd':50}]
####################
    def __init__(self, unit, pos, board):
        self.pv = self.units[0]['pv']
        self.pos = pos
        self.unit = unit
        self.type = "unit"
        super().__init__(pos, board)
####################

####################
    def disp_position(self, board):
        unit = board.getElement((self.pos[0],self.pos[1]))
        print("{}:{}".format(self.pos[0],self.pos[1]))
####################

####################
    def move(self, new_pos, board, all):

        dir=0
        horizontal = True
        vertical = True

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

            if horizontal and (dir or not vertical):
                #horizontal
                x=self.pos[0]+dirH
                y=self.pos[1]

                if (x,y) in board.elements:
                    horizontal = False
                    x=self.pos[0]
                else :
                    vertical=True

            if vertical and (not dir or not horizontal):
                #vertical
                x=self.pos[0]
                y=self.pos[1]+dirV

                if (x,y) in board.elements:
                    vertical = False
                    y=self.pos[1]
                else :
                    horizontal=True

            if (not horizontal) and (not vertical):
                break

            board.removeElement(self.pos)
            self.pos=(x,y)
            board.addElement(self.pos, self)

            dir=1-dir

            for i in range(0,20):
                for j in range(0,20):
                    if (i,j) in board.elements:
                        print(board.elements[(i,j)].team, end="\t")
                    else:
                        print("_", end="\t")
                print("")
            print()

            sleep(self.units[self.unit]['spd']/100)
####################

####################
    def scan(self, board, rng):
        retour=[]

        for i in range(-rng, rng+1):
            x=self.pos[0]+i

            for j in range(-rng, rng+1):
                y=self.pos[1]+j

                if (x>=0 and y>=0) and (abs(j)+abs(i)<=rng) and (x,y)!=self.pos:

                    if (x,y) in board.elements:
                        retour.append(board.getElement((x,y)))
        return retour
####################

####################
    def selfcheck(self, board):
        if self.pvBase <=0:
            board.removeElement(self.pos)
####################

####################
    def action_control(self):
        pass
####################
