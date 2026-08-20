from dataclasses import dataclass

from examples.rate_limiter.enums import UserTier


@dataclass(frozen=True)
class RateLimitConfig:
    """Configuration for a rate limiter: max requests allowed per window."""

    max_requests: int
    window_in_seconds: int


@dataclass(frozen=True)
class User:
    user_id: str
    tier: UserTier
