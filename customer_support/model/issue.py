from __future__ import annotations

import uuid
from dataclasses import dataclass, field

from ..enums.issue_status import IssueStatus
from ..enums.issue_type import IssueType


@dataclass
class Issue:
    """A single customer-reported support ticket."""

    transaction_id: str
    issue_type: IssueType
    subject: str
    description: str
    email: str

    id: str = field(init=False)
    status: IssueStatus = field(init=False, default=IssueStatus.OPEN)
    resolution: str | None = field(default=None, init=False)
    assigned_agent_id: str | None = field(default=None, init=False)

    def __post_init__(self) -> None:
        self.id = "I" + uuid.uuid4().hex[:6]

    def __str__(self) -> str:
        return (
            f'{self.id} {{"{self.transaction_id}", "{self.issue_type.name}", '
            f'"{self.subject}", "{self.description}", "{self.email}", "{self.status.name}"}}'
        )
