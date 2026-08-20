from ..enums import ObstacleType
from ..model.ladder import Ladder
from ..model.obstacle import Obstacle
from ..model.snake import Snake


class ObstacleFactory:
    @staticmethod
    def create_obstacle(obstacle_type: ObstacleType, up: int, down: int) -> Obstacle:
        if obstacle_type == ObstacleType.SNAKE:
            return Snake(up, down)
        if obstacle_type == ObstacleType.LADDER:
            return Ladder(up, down)
        raise ValueError("Invalid obstacle type")
