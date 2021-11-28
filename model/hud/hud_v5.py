import pygame
import random

pygame.init()

#couleurs utilisées
black = (0, 0, 0)
white = (255, 255, 255)
marron = (182,121,22)
red = (200, 0, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)

#fenêtre, clock et police
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
DISPLAY_W, DISPLAY_H = pygame.display.Info().current_w, pygame.display.Info().current_h
font = pygame.font.SysFont("arial", 18)
clock = pygame.time.Clock()

#image de ressources
g_image = pygame.image.load("gold_image.png").convert_alpha()
s_image = pygame.image.load("stone_image.png").convert_alpha()
m_image = pygame.image.load("meat_image.png").convert_alpha()
w_image = pygame.image.load("wood_image.png").convert_alpha()
p_image = pygame.image.load("people_image.png").convert_alpha()
gold_image = pygame.transform.scale(g_image, (20,20))
stone_image = pygame.transform.scale(s_image, (20,20))
meat_image = pygame.transform.scale(m_image, (20,20))
wood_image = pygame.transform.scale(w_image, (20,20))
people_image = pygame.transform.scale(p_image, (20,20))

#images de batiments et de hud
barre = pygame.image.load("barre.png").convert_alpha()
house = pygame.image.load("House.png").convert_alpha()
house_rect = house.get_rect()
house_rect.center = DISPLAY_W//2, DISPLAY_H//2
house1_rect = house.get_rect()
house1_rect.center = DISPLAY_W//2-100, DISPLAY_H//2-200
house_image = pygame.transform.scale(house, (100,100))
house_image_rect = house_image.get_rect()
house_image_rect.center = DISPLAY_W//2-100, DISPLAY_H-110

#bar de santé
bar_color = (111, 210, 46)
back_bar_color = (60, 63, 60)
max_size = 100
pv_house1 = 0.1*max_size
max_pv_house = 1*max_size
pv_house2 = 0.5*max_size

#hud toujours visible
def hud_joueur():
    gold = 9999
    gold_x1, gold_x2 = 0, 30
    stone = 9999
    stone_x1, stone_x2 = 90, 120
    meat = 9999
    meat_x1, meat_x2 = 180, 210
    wood = 9999
    wood_x1, wood_x2 = 270, 300
    people = 7
    people_x1, people_x2 = 360, 390

    display.blit(house, house_rect)
    display.blit(house, house1_rect)
    display.blit(barre, (0, 0))

    pygame.draw.rect(display, black, (0, 5, 90, 20), 2)
    pygame.draw.rect(display, black, (90, 5, 90, 20), 2)
    pygame.draw.rect(display, black, (180, 5, 90, 20), 2)
    pygame.draw.rect(display, black, (270, 5, 90, 20), 2)
    pygame.draw.rect(display, black, (360, 5, 90, 20), 2)

    display.blit(gold_image, (gold_x1 + 2, 5))
    display.blit(font.render(str(gold), True, white), (gold_x2 + 2, 5))
    display.blit(stone_image, (stone_x1 + 2, 5))
    display.blit(font.render(str(stone), True, white), (stone_x2 + 2, 5))
    display.blit(meat_image, (meat_x1 + 2, 5))
    display.blit(font.render(str(meat), True, white), (meat_x2 + 2, 5))
    display.blit(wood_image, (wood_x1 + 2, 5))
    display.blit(font.render(str(wood), True, white), (wood_x2 + 2, 5))
    display.blit(people_image, (people_x1 + 2, 5))
    display.blit(font.render(str(people), True, white), (people_x2 + 2, 5))

    pygame.display.update()
    clock.tick(15)

#hud affiché lors d'un clic sur un batîment
def hud_item(name_objects):
    pygame.draw.rect(display, marron, (0, DISPLAY_H - 150, 200, 150))
    if name_objects == house_rect :
        # rectangle infos
        pygame.draw.rect(display, marron, (DISPLAY_W // 2 - 200, DISPLAY_H - 150, 400, 150))
        back_bar_position = [DISPLAY_W // 2 - 150, DISPLAY_H - 50, max_size, 5]
        bar_position = [DISPLAY_W // 2 - 150, DISPLAY_H - 50, int(pv_house1), 5]
        pygame.draw.rect(display, back_bar_color, back_bar_position)
        pygame.draw.rect(display, bar_color, bar_position)

        #affichage icône maison et nom
        display.blit(house_image, house_image_rect)
        display.blit(font.render("Habitation", True, black), (DISPLAY_W // 2 - 125, DISPLAY_H - 40))

        #affichage actions
        display.blit(meat_image, (DISPLAY_W//2-950, DISPLAY_H-140))
    elif name_objects == house1_rect:
        pygame.draw.rect(display, marron, (DISPLAY_W // 2 - 200, DISPLAY_H - 150, 400, 150))
        back_bar_position = [DISPLAY_W // 2 - 150, DISPLAY_H - 50, max_size, 5]
        bar_position = [DISPLAY_W // 2 - 150, DISPLAY_H - 50, int(pv_house2), 5]
        pygame.draw.rect(display, back_bar_color, back_bar_position)
        pygame.draw.rect(display, bar_color, bar_position)

        display.blit(house_image, house_image_rect)
        display.blit(font.render("Habitation", True, black), (DISPLAY_W // 2 - 125, DISPLAY_H - 40))

        display.blit(meat_image, (DISPLAY_W // 2 - 950, DISPLAY_H - 140))

    pygame.display.update()
    clock.tick(15)

#action si clic sur une action d'un batîment
# def action(name_action):
#     if name_action == delete:
#         print("test")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(display, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    display.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((DISPLAY_W / 2), (DISPLAY_H / 2 - 400))
    display.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", DISPLAY_W / 2 - 150, DISPLAY_H / 2 - 300, 250, 50, blue, bright_blue, unpause)
        button("Sauvegarder la partie", DISPLAY_W / 2 - 150, DISPLAY_H / 2 - 200, 250, 50, red, bright_red, unpause)
        button("Quit", DISPLAY_W / 2 - 150, DISPLAY_H / 2 - 100, 250, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)
    display.fill(white)

def game_loop():
    global pause
    gameExit = False
    display.fill(white)

    while not gameExit:
        # display.fill(white)
        hud_joueur()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if house_rect.center[0]-80 <= pos[0] <= house_rect.center[0]+80 and house_rect.center[1]-80 <= pos[1] <= house_rect.center[1]+80:
                    hud_item(house_rect)
                elif house1_rect.center[0]-80 <= pos[0] <= house1_rect.center[0]+80 and house1_rect.center[1]-80 <= pos[1] <= house1_rect.center[1]+80:
                    hud_item(house1_rect)
                else:
                    display.fill(white)
                    hud_joueur()
                    pygame.display.update()
                    clock.tick(60)


        pygame.display.update()
        clock.tick(60)

game_loop()
