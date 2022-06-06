import random
import pickle

from constants import COLS, POPULATION_SIZE, NUMBER_OF_TRAILS


def m_not_around_m2(tablica, m, m2, n):
    k = 0
    number_of_m2 = 0
    for i in range(n):
        for j in range(n):
            if tablica[i][j] == m2:
                number_of_m2 += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    if match(tablica, i + dx, j + dy, m, n):
                        pass
                    else:
                        k += 1
    if number_of_m2 != 0:
        return round((1 - (k / (8 * number_of_m2))), 3)
    return 1


def match(tablica, x, y, m, n):
    if x < 0 or y < 0:
        return True
    if x > n - 1 or y > n - 1:
        return True
    if tablica[x][y] == m:
        return False
    return True


def m_not_over_edge(tablica, m, n):
    sum = 1

    for i in range(n):
        for j in range(n):
            if tablica[i][j] == m:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if match2(i + dx, j + dy, n):
                        pass
                    else:
                        sum -= 1 / (4 * (n - 1))
    return round(sum, 3)


def match2(x, y, n):
    if x < 0 or y < 0:
        return False
    if x > n - 1 or y > n - 1:
        return False
    return True


def max_k_vegetables_in_group(tablica, k, m, n):
    id = 0
    sum = 0
    l = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if tablica[i][j] == m and visited[i][j] == 0:
                l += 1
                ile = dfs(tablica, i, j, visited, m, n)
                if ile > k:
                    id = 1
                    sum += 2 ** ((-1) * ile + k)

    if id == 0:
        return 1
    return round(sum / l, 3)


def match3(tablica, x, y, m, n):
    if x < 0 or y < 0:
        return False
    if x > n - 1 or y > n - 1:
        return False
    if tablica[x][y] == m:
        return True
    return False


def dfs(tablica, x, y, visited, m, n):
    visited[x][y] = 1
    odw = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if match3(tablica, x + dx, y + dy, m, n) and visited[x + dx][y + dy] == 0:
            odw += dfs(tablica, x + dx, y + dy, visited, m, n)
    return odw
