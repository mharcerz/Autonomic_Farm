import pygame
from constants import BACKGROUND, ROWS, COLS, SQUARE_SIZE, WIDTH, HEIGHT, WHITE
from field import Field
from loader import tractor
from tractor import Tractor


class Board:
    def __init__(self, window):
        self.board = []
        self.window = window
        self.window.fill(BACKGROUND)

    def draw_tractor(self):
        sprites = pygame.sprite.Group()

        tractor = Tractor()

        sprites.add(tractor)

        sprites.draw(self.window)

        # self.window.blit(image, ((ROWS - 1) * SQUARE_SIZE, (COLS - 1) * SQUARE_SIZE))

    def select_square(self, row, col):
        rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

        # tworzenie objektu pole po kliknieciu
        field = Field(row, col)

        # tworzenie klucza do słownika zawierającego wszystkie pola
        wspolrzedna = str(row) + "," + str(col)
        Field.addFieldToDict(Field.allFieldsDictionary, wspolrzedna, field)

        # odwoływanie się do pojedyńczego pola w słowniku
        # można to ewentualnie poprawić na odwoływanie przez float a nie string
        # Field.allFields["0,0"].fieldParameters()

        # funkcja do wypisania wszystkich pól dodanych do słownika
        # Field.printAllFieldsParameters(Field.allFields)

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
