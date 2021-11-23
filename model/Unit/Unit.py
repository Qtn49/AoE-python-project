"""
Import
"""
from time import sleep
from model.Map import *
from model.Unit.Variables import *
from model.Element import Element
from model.game_constants import *


class Unit(Element):
    """
	Possible actions for Units (moving, attack...)
	"""

    def __init__(self, pos, team):
        """
		Create unit
		"""
        self.type = "unit"
        self.team = team
        self.moveX = 0
        self.moveY = 0
        super().__init__(pos)

    def control(self, x, y):
        """
		Control Player
		"""
        self.moveX += x
        self.moveY += y
        sleep(1 / self.spd)

    def update(self):
        """
		update sprite position
		"""
        board = Map.get_map()
        newX = self.pos[0] + self.moveX
        newY = self.pos[1] + self.moveY

        board.addElement((newX, newY), self)
        board.removeElement(self.pos)

        self.pos[0] = newX
        self.pos[1] = newY

        # # moving left
        # if self.moveX < 0:
        #     self.image = self.images[self.frame // ani]
        #
        # # moving right
        # if self.moveX > 0:
        #     self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        self.moveX = 0
        self.moveY = 0

    def move(self, newPos):
        """
		moving without doing anything else
		"""

        # savoir où on va
        newX = legal(newPos[0])
        newY = legal(newPos[1])

        while self.pos[0] != newX or self.pos[1] != newY:

            # trouver la direction
            dir = self.direction(newX, newY)

            # se déplacer
            if not self.walk(dir):
                # s'arrêter en cas de blocage
                # print(self.rect.x, " : ", self.rect.y, " ?")
                return False

        # print(self.rect.x, " : ", self.rect.y, " ?")
        return True

    def walk(self, dir):
        """
		used to move
		"""

        # détecter les collisions
        # collide = self.choice(dirX, dirY)

        # if not collide or (collide[0] and not dirY) or (collide[1] and not dirX):
        #     print("BLOCK")
        #     return False

        butX = legal(self.pos[0]) + MODEL_DIMENSIONS[0] * dir[0]
        butY = legal(self.pos[0]) + MODEL_DIMENSIONS[1] * dir[1]

        while self.rect.x != butX or self.rect.y != butY:
            self.control(dir[0], dir[1])
            self.update()

        return True

    def direction(self, newX, newY):
        """
		defines the direction we need to take for the objective
		"""
        if self.pos[0] < newX:      dirX = 1
        elif self.pos[0] > newX:    dirX = -1
        else:                       dirX = 0

        if self.rect.y < newY:      dirY = 1
        elif self.rect.y > newY:    dirY = -1
        else:                       dirY = 0

        return (dirX, dirY)

    def march(self, target):
        """
		moving and attacking
		"""
        zone = self.scanEuc(self.rng)

        while target not in zone:
            dir = self.direction(target.rect.x, target.rect.y)
            newX = legal(self.rect.x) + dir[0] * base
            newY = legal(self.rect.y) + dir[1] * base

            if not self.move(newX, newY) and target not in zone:
                return False

            zone = self.scanEuc(self.rng)

            """
			while self.rect.x!=legal(self.rect.x)+dir[0]*base and self.rect.y!=legal(self.rect.y)+abs(dir[1])*base:
				zone = self.scanEuc(board, self.rng)
				if not self.walk(board, dir[0], dir[1]) and target not in zone:
					imp=True
					break

			if imp:
				return False
			"""

        return True

    def collision_V2(self, cX, cY):

        if (cX < 0 or cX >= base * size) or (cY < 0 or cY >= base * size):
            return True

        for sprite in board:
            if sprite != self:
                if cX >= legal(sprite.rect.left) and cX <= legal(sprite.rect.right) and cY >= legal(
                        sprite.rect.top) and cY <= legal(sprite.rect.bottom):
                    return True

        return False

    def choice(self, dirX, dirY):

        box = [False for i in range(3)]
        if dirX != 0:

            cX = legal(self.rect.x) + base * dirX
            cY = legal(self.rect.y)

            if not self.collision_V2(cX, cY):
                box[0] = True
            # print("H")

            if dirY != 0:
                cY = legal(self.rect.y) + base * dirY

                if not self.collision_V2(cX, cY):
                    box[2] = True
                # print("D")

                cX = legal(self.rect.x)

                if not self.collision_V2(cX, cY):
                    box[1] = True
                # print("V")

        elif dirY != 0:
            cX = legal(self.rect.x)
            cY = legal(self.rect.y) + base * dirY

            if not self.collision_V2(cX, cY):
                box[1] = True
                print("V")

        if not box[0] and not box[1] and not box[2]:
            return False

        if box[2]:
            return (0, 0)
        elif box[0]:
            return (0, 1)
        elif box[1]:
            return (1, 0)
        else:
            return (1, 1)

    def scanEuc(self, rng):
        """
		to know what's around you
		"""
        retour = []

        for i in range(-rng, rng + 1):
            x = legal(self.rect.x) + i * base

            for j in range(-rng, rng + 1):
                y = legal(self.rect.y) + j * base

                for ob in board:
                    if legal(ob.rect.x) == x and legal(ob.rect.y) == y and ob != self:
                        retour.append(ob)
        return retour

    def scanMan(self, rang):
        """
		to know what's around you
		"""
        retour = []

        for i in range(-rang, rang + 1):
            x = legal(self.rect.x) + i * base

            for j in range(-rang, rang + 1):
                y = legal(self.rect.y) + j * base

                if abs(i) + abs(j) <= rang and (x, y) != (self.rect.x, self.rect.y):
                    for ob in board:
                        if legal(ob.rect.x) == x and legal(ob.rect.y) == y:
                            retour.append(ob)
        return retour

    def attack(self, target):
        """
		attacking
		"""

        # validation
        if not (target in board and (target.type == "batiment" or target.type == "unit") and target.team != self.team):
            return False

        # sauvegarder
        self.cache = self.action
        self.action = "atk"

        while target.pv > 0 and self.action == "atk":
            sleep(1 / 1000)

            # se déplacer
            if not self.march(target):
                self.action = "Neant"
                break
            target.pv -= self.atk
            target.selfcheck()
            sleep(100 / self.atk_spd)

        self.action = self.cache

    def selfcheck(self):
        """
		state checking
		"""
        print(self.team, " : ", self.pv)

        if self.pv <= 0:
            print("t'as dead ça chakal")
            if self in board:
                # print("t'as dead ça chakal")
                board.remove(self)
                self.action = "Neant"
        else:
            self.defend(self.rect.x, self.rect.y)

    def defend(self, newX, newY):
        """
		defend a position
		"""
        self.action = "defend"
        self.move(newX, newY)

        while (self.action == "defend"):
            sleep(tempo)
            zone = self.scanMan(self.sight)
            for ob in zone:
                if ob.type == "batiment" or ob.type == "unit" and ob.team != self.team:
                    self.attack(ob);
