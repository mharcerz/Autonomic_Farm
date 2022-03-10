import pygame
from constants import BACKGROUND, ROWS, SQUARE_SIZE, WIDTH, HEIGHT, WHITE


class Board:
    def __init__(self, window):
        self.board = []
        self.window = window
        self.window.fill(BACKGROUND)

    def draw_tractor(self):
        image = pygame.image.load('MinecraftCart.jpg')
        image = pygame.transform.scale(image, (100, 100))

        self.window.blit(image, (7 * SQUARE_SIZE, 7 * SQUARE_SIZE))

    def select_square(self, row, col):
        rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

        if rect in self.board:
            pygame.draw.rect(self.window, BACKGROUND, rect)
            self.board.remove(rect)
        else:
            self.board.append(rect)
            pygame.draw.rect(self.window, WHITE, rect)

        self.draw_grid()

    def draw_grid(self):
        x, y = 0, 0

        for row in range(ROWS):
            x += SQUARE_SIZE
            y += SQUARE_SIZE

            pygame.draw.line(self.window, (0, 0, 0), (x, 0), (x, WIDTH))
            pygame.draw.line(self.window, (0, 0, 0), (0, y), (HEIGHT, y))

    def update(self):
        self.draw_tractor()
        pygame.display.update()
