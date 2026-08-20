from __future__ import annotations

from ..model.agent import Agent


class AgentRepository:
    """In-memory store for Agent entities, keyed by agent id."""

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def save(self, agent: Agent) -> None:
        self._agents[agent.id] = agent

    def get_by_id(self, agent_id: str) -> Agent | None:
        return self._agents.get(agent_id)

    def get_all(self) -> list[Agent]:
        return list(self._agents.values())
