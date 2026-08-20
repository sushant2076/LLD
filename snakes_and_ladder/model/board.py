import math
from typing import Iterable, List

from ..enums import ObstacleType
from .cell import Cell
from .obstacle import Obstacle
from .player import Player


class Board:
    def __init__(self, size: int):
        self.size = size
        self.side_length = int(math.isqrt(size))
        self.grid: List[List[Cell]] = [
            [None] * self.side_length for _ in range(self.side_length)  # type: ignore
        ]

        position = 1
        left_to_right = True

        for i in range(self.side_length - 1, -1, -1):
            if left_to_right:
                for j in range(self.side_length):
                    self.grid[i][j] = Cell(position)
                    position += 1
            else:
                for j in range(self.side_length - 1, -1, -1):
                    self.grid[i][j] = Cell(position)
                    position += 1
            left_to_right = not left_to_right

    def _get_row(self, position: int) -> int:
        row = (position - 1) // self.side_length
        return self.side_length - 1 - row

    def _get_col(self, position: int) -> int:
        row = self._get_row(position)
        col = (position - 1) % self.side_length
        return self.side_length - 1 - col if row % 2 == 0 else col

    def _get_cell(self, position: int) -> Cell:
        return self.grid[self._get_row(position)][self._get_col(position)]

    def add_obstacle(self, obstacle: Obstacle) -> bool:
        src_cell = self._get_cell(obstacle.src)
        dest_cell = self._get_cell(obstacle.dest)

        if src_cell.has_obstacle() or dest_cell.has_obstacle():
            return False  # Prevents overlapping obstacles

        src_cell.obstacle = obstacle
        return True

    def get_new_position(self, player: Player, offset: int) -> int:
        new_position = player.position + offset

        if new_position > self.size:
            print("You are going out of the board! Better luck next time!")
            return player.position

        cell = self.grid[self._get_row(new_position)][self._get_col(new_position)]
        final_position = cell.get_final_position()

        if final_position < new_position:
            print(f"Oops! Snake has bitten {player.name}")
        elif final_position > new_position:
            print(f"Congratulations! {player.name} moved up through a ladder")
        else:
            print(f"{player.name} moved from {player.position} to {new_position}")

        return final_position

    def print_board(self, players: Iterable[Player]) -> None:
        print("\nCurrent Board State:")

        players = list(players)

        for i in range(self.side_length):
            row_parts = []
            for j in range(self.side_length):
                position = self.grid[i][j].position
                cell_content = str(position)

                if self.grid[i][j].has_obstacle():
                    obstacle = self.grid[i][j].obstacle
                    prefix = "S" if obstacle.obstacle_type == ObstacleType.SNAKE else "L"
                    cell_content = f"{prefix}{obstacle.dest}"

                for player in players:
                    if player.position == position:
                        cell_content = player.name

                row_parts.append(f"{cell_content:<8}")
            print("".join(row_parts))
        print()
