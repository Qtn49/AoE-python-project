#!/usr/bin/env python3

from Map import *
from Element import *
from Unit import *
from Moveable import *
from threading import *

units =[{'pv':25,'atk':3,'atk_spd':50,'rng':1,'sight':4,'spd':50}]

board = Map()
vilR = Unit(0,"Rouge",(0,0),board)
vilB = Unit(0,"Bleu", (5,5), board)

Thread(target=vilB.defend, args=((10,10),board)).start()
Thread(target=vilR.move, args=((8,8),board,False)).start()

print(board.elements)
"""
while vilB.pvBase !=0:
    vilR.attack(vilB, board)
"""
for i in range(0,20):
    for j in range(0,20):
        if (i,j) in board.elements:
            print(board.elements[(i,j)].team, end="\t")
        else:
            print("_", end="\t")
    print("")
