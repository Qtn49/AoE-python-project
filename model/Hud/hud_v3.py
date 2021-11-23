import pygame
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
marron = (182,121,22)
red = (200, 0, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)

posx, posy = 400, 300

display = pygame.display.set_mode((display_width,display_height))
font = pygame.font.SysFont("Arial", 15)
clock = pygame.time.Clock()

pause = False

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

# class Hud():
#     def __init__(self):
#         self.pause = False

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

    pygame.draw.rect(display, (0, 255, 0), (posx, posy, 30, 30))

    pygame.draw.rect(display, marron, (0, 0, 460, 30))
    pygame.draw.rect(display, black, (0, 5, 90, 20), 1)
    pygame.draw.rect(display, black, (90, 5, 90, 20), 1)
    pygame.draw.rect(display, black, (180, 5, 90, 20), 1)
    pygame.draw.rect(display, black, (270, 5, 90, 20), 1)
    pygame.draw.rect(display, black, (360, 5, 90, 20), 1)

    display.blit(gold_image, (gold_x1 + 2, 5))
    display.blit(font.render(str(gold), False, black), (gold_x2 + 2, 5))
    display.blit(stone_image, (stone_x1 + 2, 5))
    display.blit(font.render(str(stone), False, black), (stone_x2 + 2, 5))
    display.blit(meat_image, (meat_x1 + 2, 5))
    display.blit(font.render(str(meat), False, black), (meat_x2 + 2, 5))
    display.blit(wood_image, (wood_x1 + 2, 5))
    display.blit(font.render(str(wood), False, black), (wood_x2 + 2, 5))
    display.blit(people_image, (people_x1 + 2, 5))
    display.blit(font.render(str(people), False, black), (people_x2 + 2, 5))

    # display.blit(font.render('Or : ', False, black), (gold_x1 + 2, 5))
    # display.blit(font.render(str(gold), False, black), (gold_x2 + 2, 5))
    # display.blit(font.render('Pierre : ', False, black), (iron_x1 + 2, 5))
    # display.blit(font.render(str(iron), False, black), (iron_x2 + 2, 5))
    # display.blit(font.render('Viande : ', False, black), (meat_x1 + 2, 5))
    # display.blit(font.render(str(meat), False, black), (meat_x2 + 2, 5))
    # display.blit(font.render('Bois : ', False, black), (wood_x1 + 2, 5))
    # display.blit(font.render(str(wood), False, black), (wood_x2 + 2, 5))
    # display.blit(font.render('Habitants : ', False, black), (people_x1 + 2, 5))
    # display.blit(font.render(str(people), False, black), (people_x2 + 2, 5))

    pygame.display.update()
    clock.tick(15)

def hud_item():
    pygame.draw.rect(display, marron, (0, 450, 800, 150))
    pygame.draw.rect(display, black, (0, 450, 200, 150), 1)
    pygame.draw.rect(display, black, (200, 450, 400, 150), 1)
    pygame.draw.rect(display, black, (600, 450, 200, 150), 1)

    pygame.display.update()
    clock.tick(15)

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
    display.fill(white)

def paused():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    display.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, blue, bright_blue, unpause)
        button("Options", 350, 450, 100, 50, red, bright_red, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)
    display.fill(white)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Age of Cheap", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        display.blit(TextSurf, TextRect)

        button("Start", 150, 450, 100, 50, blue, bright_blue, game_loop)
        button("Quitter", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

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
                if posx - 30 <= pos[0] <= posx + 30 and posy - 30 <= pos[1] <= posy + 30:
                    hud_item()

                else:
                    display.fill(white)
                    hud_joueur()
                    pygame.display.update()
                    clock.tick(60)

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
