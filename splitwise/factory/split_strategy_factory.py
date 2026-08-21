"""SplitStrategyFactory: maps a SplitType to its SplitStrategy implementation."""

from splitwise.enums.split_type import SplitType
from splitwise.strategy.equal_split_strategy import EqualSplitStrategy
from splitwise.strategy.exact_split_strategy import ExactSplitStrategy
from splitwise.strategy.percentage_split_strategy import (
    PercentageSplitStrategy,
)
from splitwise.strategy.split_strategy import SplitStrategy


class SplitStrategyFactory:
    @staticmethod
    def get_strategy(split_type: SplitType) -> SplitStrategy:
        if split_type is SplitType.EQUAL:
            return EqualSplitStrategy()
        if split_type is SplitType.PERCENTAGE:
            return PercentageSplitStrategy()
        if split_type is SplitType.EXACT:
            return ExactSplitStrategy()
        raise ValueError(f"Unsupported split type: {split_type}")
