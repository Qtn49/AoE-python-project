import pygame
import pyscroll
import pytmx

from player import Player

class Game:

    # fonction au chargement du jeu
    def __init__(self): #
        self.screen = pygame.display.set_mode((1300, 650))  # créer la fenêtre du jeu, renvoie la surface = fenêtre
        pygame.display.set_caption("Age of Python")

        #charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx') #spécifier le fichier contenant la carte
        map_data = pyscroll.data.TiledMapData(tmx_data) #récupérer les données du tmx pour extraire la carte
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size()) #charger les calques créés à l'intérieur de la carte
        map_layer.zoom = 0.5

        # générer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        #définir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3) #assemblage des calques de tuiles en un groupe
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def update(self):
        self.group.update()

        #vérification de la collision avec l'environnement
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True
        while running:

            self.player.save_location()

            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen) #dessin des calques dans la fenêtre
            pygame.display.flip() #permet d'actualiser la carte en temps réel à chaque tour de boucle

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
