#!/usr/bin/env python3

from Map import *
from Element import *
from Moveable import *

class Unit(Moveable):

    action = 0
    type = 'unit'

####################
    def __init__(self, unit, team, pos, board):
        self.team = team
        super().__init__(unit, pos, board)
####################

####################
    def attack(self, object, board):
        self.move(object.pos, board, True)
        zone=self.scan(board, self.rng)

        target = None

        for ob in zone:
            if (board.elements[ob].type=='unit') and (board.elements[ob].team!=self.team):
                target = board.elements[ob]
                break

        if target:
            target.pvBase-=self.atk

        target.selfcheck(board)
####################

####################
    def defend(self, pos, board):
        self.action =1
        while(self.action==1):
            self.move(pos, board, False)
            zone=self.scan(board,10)
            for ob in zone:
                if board.elements[ob].team!=self.team:
                    self.attack[ob]
####################
