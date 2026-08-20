from __future__ import annotations

from ...model.agent import Agent
from ...model.issue import Issue
from .assignment_strategy import AssignmentStrategy


class DefaultAssignmentStrategy(AssignmentStrategy):
    """Assigns the issue to the first available agent whose expertise matches."""

    def assign(self, agents: list[Agent], issue: Issue) -> Agent | None:
        for agent in agents:
            if agent.is_available() and issue.issue_type in agent.expertise:
                return agent
        return None
