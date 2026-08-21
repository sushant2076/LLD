"""ExactSplitStrategy: splits the amount using exact per-user amounts supplied
via ``metadata`` (which must sum to ``total_amount``).

This strategy is not present in the original Java source (which only defines
EQUAL and PERCENTAGE) but is added here for completeness, following the same
Strategy-pattern shape as its siblings.
"""

from splitwise.model.split import Split
from splitwise.model.user import User
from splitwise.strategy.split_strategy import SplitStrategy

_EPSILON = 1e-6


class ExactSplitStrategy(SplitStrategy):
    def split(
        self,
        total_amount: float,
        participants: list[User],
        metadata: dict[User, float] | None,
    ) -> list[Split]:
        metadata = metadata or {}
        total_exact = sum(metadata.get(user, 0.0) for user in participants)
        if abs(total_exact - total_amount) > _EPSILON:
            raise ValueError("Sum of exact amounts should equal total amount")

        return [Split(user, metadata.get(user, 0.0)) for user in participants]
