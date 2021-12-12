import pygame.mouse

from model.building.Barracks import Barracks
from model.building.House import House
from model.building.TourArcher import TourArcher
from resources.Console import *
from resources.Horloge import *
from model.Unit.Villager import *
from model.Unit.Player import *
from model.building.Forum import *
from model.building.Tree import *
from view.Map_erle import MapE
from view.hud.hud import *
from resources.game_constants import *
from model.Unit.Champion import *
from model.Unit.King import *
from model.age.Age import *
from view.menu import MainMenu

def createWave(time, number, board, h, forum):
    sleep(3)
    for i in range(number):
        for j in range(5+i):
            c = Champion((4200-i*3*BASE, 450+j*2*BASE+i*BASE),'B', board, time)
            c.thr = Threadatuer(target=c.defend, args=(c.x, c.y, h, forum)).start()
            board.board.append(c)
        for j in range(4+i):
            c = Champion((4200-i*3*BASE+2*BASE+j*2*BASE, 450+(6-2)*2*BASE+i*3*BASE),'B', board, time)
            c.thr = Threadatuer(target=c.defend, args=(c.x, c.y, h, forum)).start()
            board.board.append(c)
    board.update_afg()

def collision(self, cX, cY, board):
    # limites de la map
    if (cX < 0 or cX >= (GAME_DIMENSIONS[0] - self.size + 1) * BASE) or (cY < 0 or cY >= (GAME_DIMENSIONS[1] - self.size + 1) * BASE):
        return True

    # collision avec les sprites
    for sprite in board.board:
        if legal(sprite.x) <= cX <= legal(sprite.x) + (sprite.size - 1) * BASE or legal(sprite.x) <= cX + (
                self.size - 1) * BASE <= legal(sprite.x) + (sprite.size - 1) * BASE:
            if legal(sprite.y) <= cY <= legal(sprite.y) + (sprite.size - 1) * BASE or legal(
                    sprite.y) <= cY + (self.size - 1) * BASE <= legal(sprite.y) + (
                    sprite.size - 1) * BASE:
                return True

    return False

def cadrillage(world):
    nb_X = WIDTH // BASE
    nb_Y = HEIGHT // BASE

    for i in range(1,nb_X+1):
        pygame.draw.line(world, (105, 105, 105), (i * BASE, 0), (i * BASE, HEIGHT), width=1)
    for i in range(1, nb_Y + 1):
        pygame.draw.line(world, (105, 105, 105), (0, i * BASE), (WIDTH, i * BASE), width=1)


def main():
    thr = []
    fetchable=("tree", "stonemine", "goldmine", "animal")
    fightable = ("house", "tourarcher", "tourarcher", "forum", "villager", "knight", "champion", "bigdaddy")

    board = MapE()
    counter = 0
    vague = {10:True, 20:True, 25:True, 30:True}

    age = Age()
    cache_clk = None
    hudsprites = None
    target = [0, 0]
    world = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()
    pygame.init()

    d = MainMenu()
    d.display_menu()
    joueur1 = d.joueur

    hud = Hud()
    console = Console()

    horloge = Horloge()
    hthr = Threadatuer(target=horloge.horloge, args=())
    hthr.start()

    if d.from_saved_game:
         board = board.create_map_from_file('last_game.json', joueur1)
    else:
         board = board.create_map_from_file('map_n.png', joueur1)
    game = True

    # les deux sont placés avant car trop pénible de chercher dans le tableau map
    forum = Forum((500,4500),'R',joueur1, board)
    board.board.append(forum)
    king = King((4500, 500), 'B', board)
    board.board.append(king)
    board.update_afg()

    pygame.mouse.set_cursor(pygame.cursors.arrow)

    """
    Loop
    """
    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    hthr.tuer()
                    for ob in board.board:
                        if ob.thr:
                            ob.thr.tuer()
                    game=False

                if event.key == pygame.K_UP:
                    board.move_screen(0, -1)
                if event.key == pygame.K_DOWN:
                    board.move_screen(0, 1)
                if event.key == pygame.K_LEFT:
                    board.move_screen(-1, 0)
                if event.key == pygame.K_RIGHT:
                    board.move_screen(1, 0)
                if event.key == ord('z'):
                    age.changement(joueur1, forum)
                if event.key == ord('m'):
                    cthr = Threadatuer(target=console.console, args=(joueur1, horloge, board))
                    cthr.start()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s] and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    board.create_json_file("last_game")


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clk_sprites = [s for s in board.afg if s.rect.collidepoint(pos)]

                target[0]=pos[0]+board.screenX
                target[1]=pos[1]+board.screenY

                # click_manager(clk_sprites, target)
                if cache_clk:
                    if not clk_sprites:
                        if cache_clk.type == "unit":
                            if cache_clk.thr:
                                cache_clk.thr.tuer()
                                cache_clk.thr=None
                                for i in cache_clk.action:
                                    cache_clk.action[i] = False
                            cache_clk.thr = Threadatuer(target=cache_clk.move, args=(target[0], target[1])).start()
                            cache_clk = None
                    else:
                        if clk_sprites[0].job in fightable:
                            if clk_sprites[0].team != cache_clk.team:
                                if cache_clk.thr:
                                    cache_clk.thr.tuer()
                                    for i in cache_clk.action:
                                        cache_clk.action[i] = False
                                cache_clk.thr = Threadatuer(target=cache_clk.attack, args=(clk_sprites[0],)).start()
                                cache_clk = None

                if clk_sprites:
                    hudsprites = clk_sprites[0]
                    if clk_sprites[0].type == "unit":
                        cache_clk = clk_sprites[0]
                    if clk_sprites[0].job in fetchable:
                        if cache_clk and cache_clk.job=="villager":
                            if cache_clk.thr:
                                cache_clk.thr.tuer()
                                for i in cache_clk.action:
                                    cache_clk.action[i] = False
                            cache_clk.thr = Threadatuer(target=cache_clk.fetch, args=(forum, clk_sprites[0], joueur1, board)).start()
                            cache_clk = None
                else:
                    hudsprites = None
                    cache_clk=None

            if event.type == pygame.KEYDOWN:
                m = None
                if event.key == ord('w'):
                    m = House((legal(target[0]), legal(target[1])), 'R', joueur1, board)

                if event.key == ord('x'):
                    m = Barracks((legal(target[0]), legal(target[1])),'R', joueur1, board)

                if event.key == ord('c'):
                    if age.agePassed:
                        m = TourArcher((legal(target[0]), legal(target[1])), 'R', joueur1, board)

                if event.key == ord('v'):
                    m = Villager((legal(target[0]), legal(target[1])), 'R', board, joueur1)

                if event.key == ord('b'):
                    kght =False
                    for i in board.board:
                        if i.job=="barracks":
                            kght=True
                    if kght :
                        m = Knight((legal(target[0]), legal(target[1])), 'R', board, joueur1)

                if event.key == ord('n'):
                    m = Champion((legal(target[0]), legal(target[1])), 'B', board, joueur1)

                if m and not collision(m, target[0], target[1], board) :
                    if (m.needFood <= joueur1.contenu["food"] and m.needInhabitant <= joueur1.contenu["inhabitant"] and m.needGold <= joueur1.contenu["gold"] and m.needStone <= joueur1.contenu["stone"] and m.needWood <= joueur1.contenu["wood"]):
                        joueur1.contenu["food"] -= m.needFood
                        joueur1.contenu["inhabitant"] -= m.needInhabitant
                        joueur1.contenu["gold"] -= m.needGold
                        joueur1.contenu["wood"] -= m.needWood
                        joueur1.contenu["stone"] -= m.needStone
                        board.board.append(m)


        if vague[10] and horloge.minute==10:
            for ob in board.board :
                if ob.job=="champion" and ob.vague==10:
                    ob.cacheTarget = forum
                    ob.thr = Threadatuer(target=ob.defend, args=(forum.x,forum.y)).start()
            thr.append(Threadatuer(target=createWave, args=(20,2,board,horloge, forum)).start())
            vague[10]=False

        if vague[20] and horloge.minute == 20:
            for ob in board.board:
                if (ob.job == "champion" or ob.job=="king") and ob.vague == 20:
                    ob.action = {"atk": False, "defend": False, "Construction": False, "fetch": False}
                    sleep(1)
                    # ob.cacheTarget = forum
                    # ob.thr = Threadatuer(target=ob.defend, args=(forum.x, forum.y)).start()
            vague[20] = False
        mouse_pos = pygame.mouse.get_pos()



        if counter == 0:
            if mouse_pos[0] < 30:
                board.move_screen(-1, 0)
            if mouse_pos[1] < 30:
                board.move_screen(0, -1)
            if mouse_pos[0] > WIDTH - 30:
                board.move_screen(1, 0)
            if mouse_pos[1] > HEIGHT - 30:
                board.move_screen(0, 1)
        counter += 1

        if counter == 2:
            counter = 0

        world.fill((152, 251, 152))
        cadrillage(world)


        board.update_afg()

        board.afg.draw(world)
        hud.hud_joueur(world, joueur1, horloge)

        if hudsprites:
            hud.hud_item(world, hudsprites)


        if king.pv <= 0:
            img = pygame.image.load(os.path.join("resources/gagner.png")).convert()
            world.blit(img, (500, 500))
            pygame.display.update()
            game=False
            sleep(2)
            pygame.quit()
            hthr.tuer()
            for ob in board.board:
                if ob.thr:
                    ob.thr.tuer()
        if forum.pv <= 0:
            img = pygame.image.load(os.path.join("resources/perdu.png")).convert()
            world.blit(img, (500, 500))
            pygame.display.update()
            game=False
            sleep(2)
            pygame.quit()
            hthr.tuer()
            for ob in board.board:
                if ob.thr:
                    ob.thr.tuer()
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    hthr.tuer()
    for ob in board.board:
        if ob.thr:
            ob.thr.tuer()

if __name__ == '__main__': main()
