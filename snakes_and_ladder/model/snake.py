from ..enums import ObstacleType
from .obstacle import Obstacle


class Snake(Obstacle):
    def __init__(self, head: int, tail: int):
        super().__init__(head, tail)

    @property
    def obstacle_type(self) -> ObstacleType:
        return ObstacleType.SNAKE
