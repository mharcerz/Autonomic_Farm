from constants import WIDTH, HEIGHT
from game import Game


def main():
    game = Game(WIDTH, HEIGHT)
    game.game_loop()


if __name__ == "__main__":
    main()
