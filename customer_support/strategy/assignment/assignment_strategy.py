from __future__ import annotations

from abc import ABC, abstractmethod

from ...model.agent import Agent
from ...model.issue import Issue


class AssignmentStrategy(ABC):
    """Strategy interface for choosing which agent should handle an issue."""

    @abstractmethod
    def assign(self, agents: list[Agent], issue: Issue) -> Agent | None:
        """Return an available agent to handle the issue, or None if none is found."""
        raise NotImplementedError
