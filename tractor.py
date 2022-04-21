import copy
from operator import itemgetter

import pygame

import constants
from constants import *
from field import Field
from loader import tractor


class Tractor(pygame.sprite.Sprite):
    def __init__(self, window, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(tractor, (SQUARE_SIZE, SQUARE_SIZE))
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

    @staticmethod  # sprawdza czy dany ruch które chce wykonać traktor jest możliwy, zwraca pozycje po wykonaniu ruchu
    def is_move_allowed_succ(node):
        if node.get_direction() == DIRECTION_EAST and node.get_y() * BLOCK_SIZE + BLOCK_SIZE < WIDTH:
            return "x + 1"  # jeśli ten ruch nie przekroczy mapy to jest mozliwy do wykonania
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
                    if self.direction == 5:
                        self.direction = 1
                elif move == "rotate_left":
                    self.direction -= 1
                    if self.direction == 0:
                        self.direction = 4

    def tractor_direction(self):
        compas = self.whichDirection(self.direction)
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


class Istate:  # stan początkowy traktora (miejsce w którym się on znajduje)
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y


class Node:  # wierzchołek grafu
    def __init__(self, action, direction, parent, x, y):
        self.action = action  # akcja jaką ma wykonać (obróc się w lewo, obróć się w prawo, ruch do przodu)
        self.direction = direction
        self.parent = parent  # ojciec wierzchołka
        self.x = x
        self.y = y

    def get_action(self):
        return self.action

    def set_action(self, action):
        self.action = action

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y


def cost(map, node):  # funkcja kosztu : ile kosztuje przejechanie przez dane pole
    cost = 0
    while (node.get_parent() != None):
        cost = cost + map.get_field_cost(int(node.get_x()), int(node.get_y())) + 1
        node = node.get_parent()
    return cost


def f(goaltest, map, node):  # funkcja zwracająca sumę funkcji kosztu oraz heurestyki
    return cost(map, node) + heuristic(goaltest, node)


def goal_test(elem, goaltest):
    # funkcja sprawdzająca czy położenie traktora równa się położeniu punktu docelowego, jeśli tak zwraca prawdę, w przeciwnym wypadku fałsz
    if elem.get_x() == goaltest[0] and elem.get_y() == goaltest[1]:
        return True
    else:
        return False


def graphsearch(explored, fringe, goaltest, istate):  # przeszukiwanie grafu wszerz
    node = Node(None, istate.get_direction(), None, istate.get_x(),
                istate.get_y())  # wierzchołek początkowy, stworzony ze stanu początkowego wózka
    fringe.append((node, 0))  # wierzchołki do odwiedzenia z priorytetem
    while True:
        if not fringe:
            return False
        elem = fringe.pop(0)  # zdejmujemy wierzchołek z kolejki fringe i rozpatrujemy go
        temp = copy.copy(elem[0])
        if goal_test(elem[0],
                     goaltest) is True:  # jeżeli osiągniemy cel w trakcie przeszukiwania grafu wszerz (wjedziemy na pole docelowe) : zwracamy listę ruchów, po których wykonaniu dotrzemy na miejsce
            return print_moves(elem[0])
        explored.append(elem)  # dodajemy wierzchołek do listy wierzchołków odwiedzonych
        for (action, state) in succ_with_obstacle(
                temp):  # iterujemy po wszystkich możliwych akcjach i stanach otrzymanych dla danego wierzchołka grafu
            fringe_tuple = []
            fringe_tuple_prio = []
            explored_tuple = []
            for (x, y) in fringe:
                fringe_tuple.append((x.get_direction(), x.get_x(), x.get_y()))
                fringe_tuple_prio.append(((x.get_direction(), x.get_x(), x.get_y()), y))
            for (x, y) in explored:
                explored_tuple.append((x.get_direction(), x.get_x(), x.get_y()))
            x = Node(action, state[0], elem[0], state[1],
                     state[2])  # stworzenie nowego wierzchołka, którego rodzicem jest elem
            # p = f(goaltest, map, x)  # liczy priorytet
            p = 0
            if state not in fringe_tuple and state not in explored_tuple:  # jeżeli stan nie znajduje się na fringe oraz nie znajduje się w liście wierzchołków odwiedzonych
                fringe.append((x, p))  # dodanie wierzchołka na fringe
                fringe = sorted(fringe, key=itemgetter(1))  # sortowanie fringe'a według priorytetu
            elif state in fringe_tuple:
                i = 0
                for (state_prio, r) in fringe_tuple_prio:
                    if str(state_prio) == str(state):
                        if r > p:
                            fringe.insert(i, (x,
                                              p))  # zamiana state, który należy do fringe z priorytetem r na state z priorytetem p (niższym)
                            fringe.pop(i + 1)  # todo użyć kolejki priorytetowej żeby nie sortować
                            fringe = sorted(fringe, key=itemgetter(1))  # sortowanie fringe'a według priorytetu
                            break
                    i = i + 1


def heuristic(goaltest, node):  # funkcja heurestyki : oszacowuje koszt osiągnięcia stanu końcowego (droga)
    return abs(node.get_x() - goaltest[0]) + abs(node.get_y() - goaltest[1])


def print_moves(elem):  # zwraca listę ruchów jakie należy wykonać by dotrzeć do punktu docelowego
    moves_list = []
    while (elem.get_parent() != None):
        moves_list.append(elem.get_action())
        elem = elem.get_parent()
    moves_list.reverse()
    return moves_list


def succ(elem):
    # funkcja następnika, przypisuje jakie akcje są możliwe do wykonania na danym polu oraz jaki będzie stan (położenie) po wykonaniu tej akcji
    actions_list = []  # todo skrócić to, bez sensu podawać dla zmiany kierunku x i y, zamiast 4 razy if wystarczy 1???
    temp = copy.copy(elem.get_direction())
    if temp == 1:
        temp = 4
    else:
        temp = temp - 1
    actions_list.append(("rotate_left", (temp, elem.get_x(), elem.get_y())))
    temp = copy.copy(elem.get_direction())
    if temp == 4:
        temp = 1
    else:
        temp = temp + 1
    actions_list.append(("rotate_right", (temp, elem.get_x(), elem.get_y())))
    temp_move_south = elem.get_y() + 1
    temp_move_west = elem.get_x() - 1
    temp_move_east = elem.get_x() + 1
    temp_move_north = elem.get_y() - 1

    if Tractor.is_move_allowed_succ(elem) == "y + 1":
        actions_list.append(("move", (elem.get_direction(), temp_move_east, elem.get_y())))
    elif Tractor.is_move_allowed_succ(elem) == "x - 1":
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_north)))
    elif Tractor.is_move_allowed_succ(elem) == "x + 1":
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_south)))
    elif Tractor.is_move_allowed_succ(elem) == "y - 1":
        actions_list.append(("move", (elem.get_direction(), temp_move_west, elem.get_y())))
    return actions_list


def succ_with_obstacle(
        elem):  # funkcja następnika, przypisuje jakie akcje są możliwe do wykonania na danym polu oraz jaki będzie stan (położenie) po wykonaniu tej akcji
    actions_list = []
    temp = copy.copy(elem.get_direction())
    if temp == 1:
        temp = 4
    else:
        temp = temp - 1
    actions_list.append(("rotate_left", (temp, elem.get_x(), elem.get_y())))
    temp = copy.copy(elem.get_direction())
    if temp == 4:
        temp = 1
    else:
        temp = temp + 1
    actions_list.append(("rotate_right", (temp, elem.get_x(), elem.get_y())))
    temp_move_south = elem.get_y() + 1
    temp_move_west = elem.get_x() - 1
    temp_move_east = elem.get_x() + 1
    temp_move_north = elem.get_y() - 1

    if Tractor.is_move_allowed_succ(elem) == "y + 1" and can_you_move_here(elem.get_x() + 1, elem.get_y()):
        actions_list.append(("move", (elem.get_direction(), temp_move_east, elem.get_y())))
    elif Tractor.is_move_allowed_succ(elem) == "x - 1" and can_you_move_here(elem.get_x(), elem.get_y() - 1):
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_north)))
    elif Tractor.is_move_allowed_succ(elem) == "x + 1" and can_you_move_here(elem.get_x(), elem.get_y() + 1):
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_south)))
    elif Tractor.is_move_allowed_succ(elem) == "y - 1" and can_you_move_here(elem.get_x() - 1, elem.get_y()):
        actions_list.append(("move", (elem.get_direction(), temp_move_west, elem.get_y())))

    return actions_list


def can_you_move_here(x, y):
    x = int(x)
    y = int(y)
    return Field.allFieldsDictionary["{},{}".format(x, y)].can_u_be_here()
