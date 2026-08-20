"""SplitStrategyFactory: maps a SplitType to its SplitStrategy implementation."""

from examples.splitwise.enums.split_type import SplitType
from examples.splitwise.strategy.equal_split_strategy import EqualSplitStrategy
from examples.splitwise.strategy.exact_split_strategy import ExactSplitStrategy
from examples.splitwise.strategy.percentage_split_strategy import (
    PercentageSplitStrategy,
)
from examples.splitwise.strategy.split_strategy import SplitStrategy


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
