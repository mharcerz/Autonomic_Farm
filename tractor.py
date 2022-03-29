import pygame
from loader import tractor
from constants import SQUARE_SIZE, ROWS, COLS


class Tractor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(tractor, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((ROWS - 1) * SQUARE_SIZE, (COLS - 1) * SQUARE_SIZE)