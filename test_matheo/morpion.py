import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                pos_joueur1 = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (255,255,255),(pos_joueur1[0], pos_joueur1[1]),50,10)
            if pygame.mouse.get_pressed() == (0,0,1):
                pos_joueur2 = pygame.mouse.get_pos()
                pygame.draw.rect(screen, (100,0,0),(pos_joueur2[0], pos_joueur2[1],95,95))

    pygame.draw.line(screen, (255, 255, 255), (266, 0), (266, 600), 2)
    pygame.draw.line(screen, (255, 255, 255), (532, 0), (532, 600), 2)
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (800, 200), 2)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 2)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
