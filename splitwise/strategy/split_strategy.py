"""SplitStrategy: the Strategy-pattern interface for splitting an expense."""

from abc import ABC, abstractmethod

from splitwise.model.split import Split
from splitwise.model.user import User


class SplitStrategy(ABC):
    @abstractmethod
    def split(
        self,
        total_amount: float,
        participants: list[User],
        metadata: dict[User, float] | None,
    ) -> list[Split]:
        """Split ``total_amount`` among ``participants``, returning one Split per user."""
        raise NotImplementedError
