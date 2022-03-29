import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board


class Game:
    def __init__(self, screen_width, screen_height):
        self.screenHeight = screen_height
        self.screenWidth = screen_width
        self.run = True
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = Board(self.window)
        self.board.draw_grid()
        pygame.display.set_caption("Autonomic Farm")

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        return row, col

    def game_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    self.board.select_square(row, col)

            self.board.update()
