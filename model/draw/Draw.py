import pygame


class Draw:
    BLACK, WHITE = (0, 0, 0), (255, 255, 255)

    def __init__(self):
        self.font_name = 'model/menu/8-BIT WONDER.TTF'

    @staticmethod
    def draw_text(text, size, x, y, display):
        # font = pygame.font.SysFont('Corbel', size)
        font = pygame.font.Font('model/menu/8-BIT WONDER.TTF', size)
        text_surface = font.render(text, True, Draw.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        display.blit(text_surface, text_rect)
        return text_rect
