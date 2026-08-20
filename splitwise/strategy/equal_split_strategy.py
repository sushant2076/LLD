"""EqualSplitStrategy: splits the amount evenly across all participants."""

from examples.splitwise.model.split import Split
from examples.splitwise.model.user import User
from examples.splitwise.strategy.split_strategy import SplitStrategy


class EqualSplitStrategy(SplitStrategy):
    def split(
        self,
        total_amount: float,
        participants: list[User],
        metadata: dict[User, float] | None,
    ) -> list[Split]:
        share = total_amount / len(participants)
        return [Split(user, share) for user in participants]
