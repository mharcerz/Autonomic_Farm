import pygame
import queue
import BFS
import constants
from constants import WIDTH, HEIGHT, SQUARE_SIZE, TRACTOR_X, TRACTOR_Y, DIRECTION_WEST
from board import Board
from tractor import Tractor, Istate, graphsearch, succ
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
    tractor = Tractor(WINDOW,  TRACTOR_X, TRACTOR_Y, constants.DIRECTION_WEST)
    board.draw_grid()
    board.draw_fields()


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

                istate = Istate(tractor.get_direction(), tractor.get_tractor_x() / constants.BLOCK_SIZE, tractor.get_tractor_y() / constants.BLOCK_SIZE)
                destination = row, col
                print("--------------------------------------------")
                tractor.tractor_direction()
                move_list = graphsearch([], [], destination, istate)
                # move_list = graphsearch([], queue.PriorityQueue(), destination, istate)
                tractor.move_tractor(row, col) #poruszanie się traktora
                board.get_square_info(row, col)
                print(move_list, "<------ move list")
                tractor.change_direction(move_list, row, col)
                tractor.tractor_direction()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    tractor.move_tractor(row, col)

        board.draw_grid()
        board.update()
        tractor.update()

    pygame.quit()





if __name__ == "__main__":
    main()
