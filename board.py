import pygame

import tractor
from tractor import Tractor
from constants import BACKGROUND, ROWS, COLS, SQUARE_SIZE, WIDTH, HEIGHT, WHITE
from field import Field


class Board:
    def __init__(self, window):
        self.board = []
        self.window = window
        self.window.fill(BACKGROUND)

    # def get_square_info(self, row, col):
    #     # tworzenie objektu pole po kliknieciu
    #     field = Field(row, col)
    #
    #     # tworzenie klucza do słownika zawierającego wszystkie pola
    #     wspolrzedna = str(row) + "," + str(col)
    #     Field.addFieldToDict(Field.allFields, wspolrzedna, field)
    #
    #     # wypisanie informacji o danym polu
    #     field.fieldParameters()
    #
    #     # odwoływanie się do pojedyńczego pola w słowniku
    #     # można to ewentualnie poprawić na odwoływanie przez float a nie string
    #     # Field.allFields["0,0"].fieldParameters()
    #
    #     # funkcja do wypisania wszystkich pól dodanych do słownika
    #     # Field.printAllFieldsParameters(Field.allFields)

    def draw_fields(self):
        for row in range(ROWS):
            for col in range(COLS):
                field = Field(row, col)
                wspolrzedna = str(row) + "," + str(col)
                Field.addFieldToDict(Field.allFields, wspolrzedna, field)
                if field.przeszkoda != 'brak':
                    self.select_square(row, col)

    def get_square_info(self, row, col):
        Field.allFields["{},{}".format(row, col)].fieldParameters()

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
        self.draw_selected_squares()

    def get_field_cost(self, x, y):  # zwraca koszt  danego pola
        return 0
