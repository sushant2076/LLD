from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field

from ..enums.issue_type import IssueType


@dataclass
class Agent:
    """A support agent capable of handling issues in certain expertise areas."""

    id: str
    email: str
    name: str
    expertise: set[IssueType]

    assigned_issue_id: str | None = None
    wait_list: deque[str] = field(default_factory=deque)
    history: list[str] = field(default_factory=list)

    def is_available(self) -> bool:
        return self.assigned_issue_id is None
