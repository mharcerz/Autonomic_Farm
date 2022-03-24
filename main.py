import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, TRACTOR_X, TRACTOR_Y
from board import Board
from tractor import Tractor
from field import Field

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


def main():
    run = True
    board = Board(WINDOW)
    tractor = Tractor(WINDOW, TRACTOR_X, TRACTOR_Y)
    board.draw_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # zakomentowanie wyłącza kolorwania pól na biało
                #board.select_square(row, col)
                board.get_square_info(row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    tractor.move_tractor(row, col)

        board.update()
        tractor.update()

    pygame.quit()


if __name__ == "__main__":
    main()
