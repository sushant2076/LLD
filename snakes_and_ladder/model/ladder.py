from ..enums import ObstacleType
from .obstacle import Obstacle


class Ladder(Obstacle):
    def __init__(self, top: int, bottom: int):
        super().__init__(bottom, top)

    @property
    def obstacle_type(self) -> ObstacleType:
        return ObstacleType.LADDER
