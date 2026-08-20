import random
from collections import deque

from ..enums import ObstacleType
from ..factory.obstacle_factory import ObstacleFactory
from ..model.board import Board
from ..model.dice import Dice
from ..model.player import Player


class Game:
    def __init__(self, size: int, no_of_ladders: int, no_of_snakes: int, no_of_dice: int):
        self.no_of_snakes = no_of_snakes
        self.no_of_ladders = no_of_ladders

        self.board = Board(size)
        self.dice = Dice(no_of_dice)
        self.players: deque[Player] = deque()

        self._init_board_obstacles()

    def _init_board_obstacles(self) -> None:
        self._generate_obstacles(self.no_of_snakes, ObstacleType.SNAKE)
        self._generate_obstacles(self.no_of_ladders, ObstacleType.LADDER)

    def _generate_obstacles(self, count: int, obstacle_type: ObstacleType) -> None:
        size = self.board.size

        while count > 0:
            up = random.randint(0, size - 2) + 2
            down = random.randint(0, up - 2) + 1

            obstacle = ObstacleFactory.create_obstacle(obstacle_type, up, down)
            if self.board.add_obstacle(obstacle):
                count -= 1

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def start_game(self) -> None:
        self.board.print_board(self.players)

        while len(self.players) > 1:
            curr_player = self.players.popleft()
            print("-----------------------------------")

            dice_roll = self.dice.roll()
            print(f"{curr_player.name} rolled {dice_roll}")

            new_position = self.board.get_new_position(curr_player, dice_roll)

            if new_position == curr_player.position:
                self.players.append(curr_player)
                continue

            curr_player.position = new_position

            if new_position == self.board.size:
                print(f"{curr_player.name} has won the game!")
            else:
                self.players.append(curr_player)

            self.board.print_board(self.players)
