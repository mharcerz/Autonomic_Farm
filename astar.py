import copy

from constants import ROWS, COLS
from field import Field
from loader import grass
from tractor import Tractor


class Istate:
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


class Node:
    def __init__(self, action, direction, parent, x, y):
        self.action = action
        self.direction = direction
        self.parent = parent
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

    def __lt__(self, other):
        return False


def f(node, destination):
    return c(node) + h(destination, node)


def c(node):
    cost = 0
    while node.get_parent() is not None:
        cost += get_field_cost(node)
        node = node.get_parent()
    return cost


def h(destination, node):
    return abs(node.get_x() - destination[0]) + abs(node.get_y() - destination[1])


def graph_search(explored, fringe, destination, initial_state):
    reset_all_fields()

    node = Node(None, initial_state.get_direction(), None, initial_state.get_x(), initial_state.get_y())

    fringe.put((0, node))

    while True:
        if fringe.empty():
            return False
        elem = fringe.get()

        if is_destination_reached(elem[1], destination) is True:
            return print_moves(elem[1])

        explored.append((elem[1].get_direction(), elem[1].get_x(), elem[1].get_y()))

        for (action, state) in succ(elem[1]):
            x = Node(action, state[0], elem[1], state[1], state[2])

            p = f(x, destination)

            if not is_in_queue(state, fringe) and state not in explored:
                fringe.put((p, x))
            elif is_in_queue(state, fringe):
                for i in range(len(fringe.queue)):
                    temp = fringe.get()
                    if (temp[1].get_direction(), temp[1].get_x(), temp[1].get_y()) == state:
                        r = temp[0]
                        if r > p:
                            fringe.put((p, x))
                            break
                    fringe.put(temp)


def succ(elem):
    actions_list = []
    direction_copy = elem.get_direction()

    if direction_copy == 1:
        direction_copy = 4
    else:
        direction_copy -= 1

    actions_list.append(("rotate_left", (direction_copy, elem.get_x(), elem.get_y())))

    direction_copy = elem.get_direction()

    if direction_copy == 4:
        direction_copy = 1
    else:
        direction_copy += 1

    actions_list.append(("rotate_right", (direction_copy, elem.get_x(), elem.get_y())))

    if Tractor.is_move_allowed_succ(elem) == "y + 1" and can_you_move_here(elem.get_x() + 1, elem.get_y()):
        actions_list.append(("move", (elem.get_direction(), elem.get_x() + 1, elem.get_y())))
    elif Tractor.is_move_allowed_succ(elem) == "x - 1" and can_you_move_here(elem.get_x(), elem.get_y() - 1):
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), elem.get_y() - 1)))
    elif Tractor.is_move_allowed_succ(elem) == "x + 1" and can_you_move_here(elem.get_x(), elem.get_y() + 1):
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), elem.get_y() + 1)))
    elif Tractor.is_move_allowed_succ(elem) == "y - 1" and can_you_move_here(elem.get_x() - 1, elem.get_y()):
        actions_list.append(("move", (elem.get_direction(), elem.get_x() - 1, elem.get_y())))

    return actions_list


def can_you_move_here(x, y):
    x = int(x)
    y = int(y)
    return Field.allFieldsDictionary["{},{}".format(x, y)].can_u_be_here()


def is_destination_reached(elem, destination):
    if elem.get_x() == destination[0] and elem.get_y() == destination[1]:
        return True
    else:
        return False


def print_moves(elem):
    moves_list = []
    while elem.get_parent() is not None:
        Field.allFieldsDictionary["{},{}".format(int(elem.get_x()), int(elem.get_y()))].set_image(grass)
        moves_list.append(elem.get_action())
        elem = elem.get_parent()
    moves_list.reverse()
    return moves_list


def reset_all_fields():
    for x in range(ROWS):
        for y in range(COLS):
            Field.allFieldsDictionary["{},{}".format(x, y)].reset_fields()


def is_in_queue(state, q):
    for x in q.queue:
        if (x[1].get_direction(), x[1].get_x(), x[1].get_y()) == state:
            return True
    return False


def get_field_cost(node):
    # if node.get_action() == "rotate_left" or node.get_direction() == "rotate_right":
    #     return 0
    return Field.allFieldsDictionary["{},{}".format(int(node.get_x()), int(node.get_y()))].getCost()
