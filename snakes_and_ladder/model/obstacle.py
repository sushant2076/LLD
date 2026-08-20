from abc import ABC, abstractmethod

from ..enums import ObstacleType


class Obstacle(ABC):
    """Base class for board obstacles (snakes and ladders)."""

    def __init__(self, src: int, dest: int):
        self.src = src
        self.dest = dest

    def move_player(self) -> int:
        return self.dest

    @property
    @abstractmethod
    def obstacle_type(self) -> ObstacleType:
        raise NotImplementedError
