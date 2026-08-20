from __future__ import annotations

from enum import Enum, auto


class IssueStatus(Enum):
    """Lifecycle states of a support issue."""

    OPEN = auto()
    IN_PROGRESS = auto()
    RESOLVED = auto()
    WAITING = auto()
