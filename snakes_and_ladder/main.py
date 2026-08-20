"""Demo entry point that simulates a full Snakes and Ladder game.

Mirrors the original Java `Main` class, but instead of reading input
interactively from the console, it runs a pre-configured simulation so it
can complete unattended.
"""

from .model.player import Player
from .service.game import Game


def run_demo() -> None:
    board_size = 100
    no_of_snakes = 5
    no_of_ladders = 5
    no_of_players = 3
    no_of_dice = 1

    game = Game(board_size, no_of_ladders, no_of_snakes, no_of_dice)

    for i in range(no_of_players):
        player = Player(f"Player{i + 1}")
        game.add_player(player)

    game.start_game()


def main() -> None:
    run_demo()


if __name__ == "__main__":
    main()
