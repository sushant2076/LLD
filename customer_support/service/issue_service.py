from __future__ import annotations

from ..enums.issue_status import IssueStatus
from ..enums.issue_type import IssueType
from ..model.issue import Issue
from ..repository.agent_repository import AgentRepository
from ..repository.issue_repository import IssueRepository


class IssueService:
    """Handles issue creation, querying, updating, and resolution."""

    def __init__(self, issue_repository: IssueRepository, agent_repository: AgentRepository) -> None:
        self._issue_repository = issue_repository
        self._agent_repository = agent_repository

    def create_issue(
        self,
        transaction_id: str,
        issue_type: IssueType,
        subject: str,
        description: str,
        email: str,
    ) -> Issue:
        issue = Issue(
            transaction_id=transaction_id,
            issue_type=issue_type,
            subject=subject,
            description=description,
            email=email,
        )
        self._issue_repository.save(issue)
        print(f'>>> Issue {issue.id} created against transaction "{transaction_id}"')
        return issue

    def get_issues(self, filter: dict[str, str]) -> list[Issue]:
        """Filter supports keys: "email", "type" (e.g. "Payment Related"), "status"."""

        def matches(issue: Issue) -> bool:
            if "email" in filter and issue.email.lower() != filter["email"].lower():
                return False
            if "type" in filter:
                expected = filter["type"].replace(" ", "_").upper()
                if issue.issue_type.name.upper() != expected:
                    return False
            if "status" in filter and issue.status.name.lower() != filter["status"].lower():
                return False
            return True

        return [issue for issue in self._issue_repository.get_all() if matches(issue)]

    def update_issue(self, issue_id: str, status: IssueStatus, resolution: str) -> None:
        issue = self._issue_repository.get_by_id(issue_id)
        if issue is None:
            raise ValueError("Issue not found")
        issue.status = status
        issue.resolution = resolution
        print(f">>> {issue_id} status updated to {issue.status.name}")

    def resolve_issue(self, issue_id: str, resolution: str) -> None:
        issue = self._issue_repository.get_by_id(issue_id)
        if issue is None:
            raise ValueError("Issue not found")

        issue.status = IssueStatus.RESOLVED
        issue.resolution = resolution

        if issue.assigned_agent_id is not None:
            agent = self._agent_repository.get_by_id(issue.assigned_agent_id)
            if agent is not None:
                agent.history.append(issue.id)
                agent.assigned_issue_id = None

        print(f">>> {issue_id} issue marked resolved")
