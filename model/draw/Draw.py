import pygame


class Draw:
    BLACK, WHITE = (0, 0, 0), (255, 255, 255)
    FONT = None
    DISPLAY = None

    def __init__(self):
        self.font_name = 'model/menu/HANDA.TTF'

    @staticmethod
    def set_display(display):
        Draw.DISPLAY = display

    @staticmethod
    def draw_text(text, size, x, y):
        # font = pygame.font.SysFont('Corbel', size)
        Draw.FONT = pygame.font.Font('model/menu/HANDA.TTF', size)
        text_surface = Draw.FONT.render(text, True, Draw.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        Draw.DISPLAY.blit(text_surface, text_rect)
        return text_rect

    @staticmethod
    def select_text(text_rect):
        if text_rect is not None:
            Draw.draw_text(">", 20, text_rect.centerx - text_rect.width / 2 - 40, text_rect.centery)
            Draw.draw_text("<", 20, text_rect.centerx + text_rect.width / 2 + 40, text_rect.centery)

    @staticmethod
    def fill(color):
        Draw.DISPLAY.fill(color)
