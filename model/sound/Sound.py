import pygame.mixer_music


class Sound:

    @staticmethod
    def playSound(path):
        pygame.mixer_music.load(path)
        pygame.mixer_music.play()
