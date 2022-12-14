from queue import PriorityQueue

import pygame

from astar import Istate, graph_search
from constants import WIDTH, HEIGHT, SQUARE_SIZE, TRACTOR_X, TRACTOR_Y, DIRECTION_WEST, BLOCK_SIZE
from board import Board
from tractor import Tractor


class Game:
    def __init__(self, screen_width, screen_height, population):
        self.screenHeight = screen_height
        self.screenWidth = screen_width
        self.run = True
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.spriteGroup = pygame.sprite.Group()

        self.board = Board(self.window)
        self.board.draw_grid()
        self.board.draw_fields(population)
        self.tractor = Tractor(self.window, TRACTOR_X, TRACTOR_Y, DIRECTION_WEST)
        self.spriteGroup.add(self.tractor)
        pygame.display.set_caption("Autonomic Farm")

    @staticmethod
    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        return row, col

    def game_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    self.board.select_square(row, col)

                    istate = Istate(self.tractor.get_direction(), self.tractor.get_tractor_x() / BLOCK_SIZE,
                                    self.tractor.get_tractor_y() / BLOCK_SIZE)
                    destination = row, col
                    print("--------------------------------------------")
                    self.tractor.tractor_direction()

                    move_list = graph_search([], PriorityQueue(), destination, istate)

                    if move_list:
                        self.tractor.move_tractor(row, col)

                    self.board.get_square_info(row, col)
                    print(move_list, "<------ move list")
                    self.tractor.change_direction(move_list, row, col)
                    self.tractor.tractor_direction()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        pos = pygame.mouse.get_pos()
                        row, col = self.get_row_col_from_mouse(pos)
                        self.tractor.move_tractor(row, col)
                    if event.key == pygame.K_q:
                        self.run = False
                if event.type == pygame.QUIT:
                    self.run = False

            self.board.update()
            self.board.draw_grid()
            self.tractor.update()

            self.board.draw()
            self.spriteGroup.draw(self.window)
