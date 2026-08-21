"""EqualSplitStrategy: splits the amount evenly across all participants."""

from splitwise.model.split import Split
from splitwise.model.user import User
from splitwise.strategy.split_strategy import SplitStrategy


class EqualSplitStrategy(SplitStrategy):
    def split(
        self,
        total_amount: float,
        participants: list[User],
        metadata: dict[User, float] | None,
    ) -> list[Split]:
        share = total_amount / len(participants)
        return [Split(user, share) for user in participants]
