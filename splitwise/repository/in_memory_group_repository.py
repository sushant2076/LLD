"""InMemoryGroupRepository: a dict-backed GroupRepository implementation."""

from examples.splitwise.model.group import Group
from examples.splitwise.repository.group_repository import GroupRepository


class InMemoryGroupRepository(GroupRepository):
    def __init__(self) -> None:
        self._store: dict[str, Group] = {}

    def find_by_id(self, id: str) -> Group | None:
        return self._store.get(id)

    def save(self, group: Group) -> None:
        self._store[group.id] = group
