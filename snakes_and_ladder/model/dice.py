import random


class Dice:
    def __init__(self, no_of_dices: int):
        self.no_of_dices = no_of_dices

    def roll(self) -> int:
        return sum(random.randint(1, 6) for _ in range(self.no_of_dices))
