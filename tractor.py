import pygame
from constants import ROWS, COLS, SQUARE_SIZE, TRACTOR_X, TRACTOR_Y, BACKGROUND
from field import Field


class Tractor:
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.draw_tractor()

    def draw_tractor(self):
        image = pygame.image.load('tractor.jpg')
        image = pygame.transform.scale(image, (100, 100))

        self.window.blit(image, (self.y, self.x))

    def move_tractor(self, next_x, next_y):
        if self.can_u_move(next_x, next_y): #jesli nie ma przeszkody to sie rusz
            self.remove_tractor(self.x, self.y)
            self.x = next_x * SQUARE_SIZE
            self.y = next_y * SQUARE_SIZE
            self.draw_tractor()


    def can_u_move(self, next_x, next_y):
        return Field.allFields["{},{}".format(next_x, next_y)].can_u_be_here()


    def update(self):
        self.draw_tractor()

    def remove_tractor(self, x, y):
        self.window.fill(BACKGROUND)
