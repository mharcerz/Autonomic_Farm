import pygame

from constants import *
from field import Field
from loader import tractor


class Tractor(pygame.sprite.Sprite):
    def __init__(self, window, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(tractor[3], (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((ROWS - 1) * SQUARE_SIZE, (COLS - 1) * SQUARE_SIZE)
        self.parent = None
        self.direction = direction  # w którą stronę traktor patrzy (DIRECTION_EAST = 2, DIRECTION_NORTH = 1, DIRECTION_SOUTH = 3, DIRECTION_WEST = 4)
        self.window = window
        self.x = x
        self.y = y

    def update_position(self):
        self.rect.topleft = (self.y, self.x)

    def move_tractor(self, next_x, next_y):
        if self.can_u_move(next_x, next_y):  # jesli nie ma przeszkody to sie rusz
            self.remove_tractor(self.x, self.y)
            self.parent = self.x, self.y
            self.x = next_x * SQUARE_SIZE
            self.y = next_y * SQUARE_SIZE
            self.update_position()

    @staticmethod
    def is_move_allowed_succ(node):
        if node.get_direction() == DIRECTION_EAST and node.get_y() * BLOCK_SIZE + BLOCK_SIZE < WIDTH:
            return "x + 1"
        elif node.get_direction() == DIRECTION_NORTH and node.get_x() * BLOCK_SIZE - BLOCK_SIZE >= 0:
            return "y - 1"
        elif node.get_direction() == DIRECTION_SOUTH and node.get_x() * BLOCK_SIZE + BLOCK_SIZE < HEIGHT:
            return "y + 1"
        elif node.get_direction() == DIRECTION_WEST and node.get_y() * BLOCK_SIZE - BLOCK_SIZE >= 0:
            return "x - 1"
        else:
            return False

    @staticmethod
    def whichDirection(direction):
        if direction == 1:
            return "NORTH"
        elif direction == 2:
            return "EAST"
        elif direction == 3:
            return "SOUTH"
        elif direction == 4:
            return "WEST"

    def change_direction(self, moves_list, next_x, next_y):
        if self.can_u_move(next_x, next_y) and moves_list != False:
            for move in moves_list:
                if move == "rotate_right":
                    self.direction += 1
                    if self.direction == 5: #TODO: ogarnąć czy nie da się tu zmienić na modulo
                        self.direction = 1
                elif move == "rotate_left":
                    self.direction -= 1
                    if self.direction == 0:
                        self.direction = 4

    def tractor_direction(self):
        compas = self.whichDirection(self.direction)
        self.image = pygame.transform.scale(tractor[self.direction - 1], (SQUARE_SIZE, SQUARE_SIZE))
        print("Kierunek w którą skierowany jest traktor to: " + compas)

    def can_u_move(self, next_x, next_y):
        return Field.allFieldsDictionary["{},{}".format(next_x, next_y)].can_u_be_here()

    def get_tractor_y(self):
        return self.y

    def get_tractor_x(self):
        return self.x

    def update(self):
        self.update_position()

    def remove_tractor(self, x, y):
        self.window.fill(BACKGROUND)

    def get_direction(self):
        return self.direction

