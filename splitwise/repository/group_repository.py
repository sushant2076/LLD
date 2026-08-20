"""GroupRepository: abstract persistence interface for Group aggregates."""

from abc import ABC, abstractmethod

from examples.splitwise.model.group import Group


class GroupRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> Group | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, group: Group) -> None:
        raise NotImplementedError
