from __future__ import annotations

from ..model.issue import Issue


class IssueRepository:
    """In-memory store for Issue entities, keyed by issue id."""

    def __init__(self) -> None:
        self._issues: dict[str, Issue] = {}

    def save(self, issue: Issue) -> None:
        self._issues[issue.id] = issue

    def get_by_id(self, issue_id: str) -> Issue | None:
        return self._issues.get(issue_id)

    def get_all(self) -> list[Issue]:
        return list(self._issues.values())
