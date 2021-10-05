#!/usr/bin/env python3

#####   Importations    #####

from time import sleep



#####       Classes     #####
#############################

class Empty:
    """Objet vide"""
    team = "neutre"
    type = "empty"



class MovingObject:
    """Objet mouvant"""

    def interact(self, board):
        """Méthode d'interaction par défaut"""
        pass

    def __init__(self, position, board):
        self.position = position
        board[self.position[0]][self.position[1]]=self

    def disp_position(self):
        print("Position : ", self.position[0],":",self.position[1])

    def move(self, new_pos, board):
        dir =0
        self.disp_position()

        horizontal = new_pos[0]-self.position[0]
        vertical = new_pos[1]-self.position[1]

        if horizontal != 0:
            unitH = int(horizontal/abs(horizontal))
        else:
            unitH = 0

        if vertical != 0:
            unitV = int(vertical/abs(vertical))
        else:
            unitV = 0

        while self.position!=new_pos:

            if horizontal!=0 and (dir==0 or vertical == 0):
                board[self.position[0]][self.position[1]]=Empty
                self.position[0]+=unitH
                horizontal-=unitH
                board[self.position[0]][self.position[1]]=self

            elif vertical!=0 and (dir==1 or horizontal == 0):
                board[self.position[0]][self.position[1]]=Empty
                self.position[1]+=unitV
                vertical-=unitV
                board[self.position[0]][self.position[1]]=self

            dir = 1-dir
            sleep(1)
            self.interact(board)
            self.disp_position()

################################################################################

class Unit(MovingObject):

    def __init__(self, type, team, position, board):
        self.type = type
        self.team = team
        super().__init__(position, board)

    def disp_unit(self):
        print("Description for : ", self.type)
        print("Team : ", self.team)
        self.disp_position()
        print("")

class Villager(Unit):

    pvBase = 100
    degatPVP = 10
    degatENV = 20
    richesse = {"or":10}

    def __init__(self, type, team, position, board, range):
        self.range = range
        super().__init__(type, team, position, board)
        self.interact(board)

    def interact(self, board):

        for i in range(self.range*2):
            for j in range(self.range*2):
                if j<0 or i<0 or (j==self.range and i==self.range):
                    pass
                else:
                    x=self.position[0]-self.range+i
                    y=self.position[1]-self.range+j
                    if board[x][y].type!="empty":
                        if board[x][y].team!=self.team:
                            print("On scan : ", x,":", y)
                            board[x][y].team=self.team
                            print(board[x][y].team)
                            print("capturé")

################################################################################

class Animal(MovingObject):

    def __init__(self, type, position, board):
        self.type = type
        super().__init__(position, board)

    def disp_animal(self):
        print("Description for : ", self.type)
        super().disp_position()
        print("")


class Sheep(Animal):

    nourriture = 100

    def __init__(self, type, position, board, team="neutre"):
        self.team = team
        super().__init__(type, position, board)

    def convert(self, team):
        self.team = team

    def disp_domestic(self):
        self.disp_animal()
        print("Team : ", self.team)


#################################
#####       Fonctions       #####
#################################

def init_board():
    board = [[Empty for i in range(10)] for j in range(10)]

    return board

def disp_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j].type,end="\t")
        print("")


#################################
#####      Programme        #####
#################################

place = init_board()

vlg_1 = Villager("chass","Rouge",[0,0], place, 3)
vlg_1.disp_unit()
disp_board(place)

anml_1 = Sheep("sheep", [5,3], place)
anml_1.disp_domestic()
disp_board(place)

vlg_1.move([3,2], place)
disp_board(place)

anml_1.disp_domestic()

print(anml_1.team)
