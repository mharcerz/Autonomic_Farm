import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    board = Board(WINDOW)
    board.draw_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                board.select_square(row, col)

        board.update()

    pygame.quit()


if __name__ == "__main__":
    main()
