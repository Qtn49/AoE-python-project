#!/usr/bin/env python3

class Element:

    def __init__(self, pos, board):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        board[pos] = self

    
