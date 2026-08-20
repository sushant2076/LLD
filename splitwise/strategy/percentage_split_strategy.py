"""PercentageSplitStrategy: splits the amount according to per-user percentages
supplied via ``metadata`` (which must sum to 100)."""

from examples.splitwise.model.split import Split
from examples.splitwise.model.user import User
from examples.splitwise.strategy.split_strategy import SplitStrategy


class PercentageSplitStrategy(SplitStrategy):
    def split(
        self,
        total_amount: float,
        participants: list[User],
        metadata: dict[User, float] | None,
    ) -> list[Split]:
        metadata = metadata or {}
        total_percent = sum(metadata.values())
        if total_percent != 100.0:
            raise ValueError("Total percent should be 100")

        return [
            Split(user, total_amount * metadata.get(user, 0.0) / 100)
            for user in participants
        ]
