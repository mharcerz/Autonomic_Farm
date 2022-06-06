import geneticAlgorithm
from constants import WIDTH, HEIGHT
from game import Game


def main():
    game = Game(WIDTH, HEIGHT)
    geneticAlgorithm.genetic_algorithm()
    game.game_loop()


if __name__ == "__main__":
    main()
