"""SplitType enum: the different strategies an expense can be split by."""

from enum import Enum, auto


class SplitType(Enum):
    EQUAL = auto()
    PERCENTAGE = auto()
    EXACT = auto()
