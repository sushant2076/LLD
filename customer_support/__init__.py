"""Customer support ticketing system LLD example.

Ported from the Java reference implementation at
org.nailyourinterview.lld.customer_support.
"""
from __future__ import annotations


from .enums.issue_status import IssueStatus
from .enums.issue_type import IssueType
from .model.agent import Agent
from .model.issue import Issue
from .repository.agent_repository import AgentRepository
from .repository.issue_repository import IssueRepository
from .service.agent_service import AgentService
from .service.assignment_service import AssignmentService
from .service.issue_service import IssueService
from .strategy.assignment.assignment_strategy import AssignmentStrategy
from .strategy.assignment.default_assignment_strategy import DefaultAssignmentStrategy

__all__ = [
    "IssueStatus",
    "IssueType",
    "Agent",
    "Issue",
    "AgentRepository",
    "IssueRepository",
    "AgentService",
    "AssignmentService",
    "IssueService",
    "AssignmentStrategy",
    "DefaultAssignmentStrategy",
]
