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


def mutation(tablica, n):
    # n to długość boku kwadratu
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)

    if tablica[x][y] > 3:
        tablica[x][y] = random.randint(4, 8)
    else:
        pass
    return tablica


def crossover(tab1, tab2, n):
    x = random.randint(-1, n - 1)
    return tab1[0:x + 1] + tab2[x + 1:n], tab2[0:x + 1] + tab1[x + 1:n]


def fitness(tablica, n):  # n - wielkość tablicy
    x = m_not_around_m2(tablica, 5, 2, n) + \
        m_not_around_m2(tablica, 6, 8, n) + \
        m_not_over_edge(tablica, 1, n) + \
        max_k_vegetables_in_group(tablica, 4, 8, n)
    return round(x, 3)


def create_populate(n, N):  # N - liczba losowych populacji
    population = [[[0] * n for _ in range(n)] for __ in range(N)]
    for k in range(N):
        for i in range(n):
            for j in range(n):
                x = random.choices([1, 2, 3, 4, 5, 6, 7, 8], weights=[1, 1, 1, 3, 3, 3, 3, 3], k=1)
                population[k][i][j] = x[0]
    return population


def how_did_it_go(population, n):
    result = []
    for i in population:
        x = fitness(i, n)
        result.append(x)
    return result


def selection(population, n):
    return random.choices(population, weights=how_did_it_go(population, n), k=2)


def run_evolution(n, N):  # N jak duża populacja
    population = create_populate(n, N)

    while N != 2 and N != 1:
        new_population = []
        selected_parent1, selected_parent2 = selection(population, 5)
        new_population.append(selected_parent1)
        new_population.append(selected_parent2)

        for j in range(int((N - 4) / 2)):
            cross_parent1, cross_parent2 = crossover(selected_parent1, selected_parent2, n)
            cross_parent1_mutation = mutation(cross_parent1, n)
            cross_parent2_mutation = mutation(cross_parent2, n)

            new_population.append(cross_parent1_mutation)
            new_population.append(cross_parent2_mutation)

        population = new_population
        N -= 2
    return max(how_did_it_go(population, n)), population[0]


def genetic_algorithm():
    print("-----------------")
    print("Begin Genetic Algorithm")
    maxi = -1
    population_with_max = -1
    gen = -1

    for i in range(NUMBER_OF_TRAILS):
        temp_max, population_temp = run_evolution(COLS,
                                                  POPULATION_SIZE)  # wielkosc kwadratu, wielkosc populacji z ktorej losujemy
        if temp_max > maxi:
            maxi = temp_max
            population_with_max = population_temp
            gen = i

    print(maxi)
    for i in population_with_max:
        print(i)
    print("W generacji nr: " + str(gen))

    with open('resources/populacja/population.txt', 'w') as f:
        for element in population_with_max:
            for i in element:
                f.write(str(i) + ', ')
            f.write('\n')
    f.close()
    print("End Genetic Algorithm")
    print("-----------------")

    return population_with_max
