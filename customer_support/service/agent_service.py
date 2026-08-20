from __future__ import annotations

import uuid

from ..enums.issue_type import IssueType
from ..model.agent import Agent
from ..repository.agent_repository import AgentRepository


class AgentService:
    """Handles agent onboarding and reporting."""

    def __init__(self, agent_repository: AgentRepository) -> None:
        self._agent_repository = agent_repository

    def add_agent(self, email: str, name: str, issue_types: list[IssueType]) -> Agent:
        agent_id = "A" + uuid.uuid4().hex[:6]
        agent = Agent(id=agent_id, email=email, name=name, expertise=set(issue_types))
        self._agent_repository.save(agent)
        print(f">>> Agent {agent_id} created")
        return agent

    def view_agents_work_history(self) -> None:
        for agent in self._agent_repository.get_all():
            print(f"{agent.id} -> {agent.history}")
