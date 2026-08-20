from __future__ import annotations

from enum import Enum, auto


class IssueType(Enum):
    """Categories of customer support issues."""

    PAYMENT_RELATED = auto()
    MUTUAL_FUND_RELATED = auto()
    GOLD_RELATED = auto()
    INSURANCE_RELATED = auto()
