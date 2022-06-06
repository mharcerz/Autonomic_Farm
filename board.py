import pygame
from pathlib import Path
from constants import BACKGROUND, ROWS, COLS, SQUARE_SIZE, WIDTH, HEIGHT, WHITE
from field import Field
import categroriseCrop

class Board(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.board = []
        self.window = window
        self.window.fill(BACKGROUND)
        self.sprites = pygame.sprite.Group()

    def draw_fields(self, population):
        for row in range(ROWS):
            for col in range(COLS):
                value = population[row][col]
                print(value)
                field = Field(row, col, value)
                self.sprites.add(field)
                wspolrzedna = str(row) + "," + str(col)
                Field.addFieldToDict(Field.allFieldsDictionary, wspolrzedna, field)

    @staticmethod
    def get_square_info(row, col):
        Field.allFieldsDictionary["{},{}".format(row, col)].fieldParameters()
        crop_source = Field.allFieldsDictionary["{},{}".format(row, col)].return_crop_source()
        crop_source = str(Path(crop_source))

        categroriseCrop.categorise_crop(crop_source)

    def select_square(self, row, col):
        rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

        if rect in self.board:
            pygame.draw.rect(self.window, BACKGROUND, rect)
            self.board.remove(rect)
        else:
            self.board.append(rect)
            pygame.draw.rect(self.window, WHITE, rect)

        self.draw_grid()

    def draw_selected_squares(self):
        # Kolorowanie przeszkód
        for square in self.board:
            pygame.draw.rect(self.window, WHITE, square)

    def draw_grid(self):
        x, y = 0, 0

        for row in range(ROWS):
            x += SQUARE_SIZE
            y += SQUARE_SIZE
            pygame.draw.line(self.window, (0, 0, 0), (x, 0), (x, WIDTH))
            pygame.draw.line(self.window, (0, 0, 0), (0, y), (HEIGHT, y))

    def update(self):
        # Aktualizacja ekranu
        pygame.display.update()
        # self.draw_selected_squares()

    def draw(self):
        self.sprites.draw(self.window)
