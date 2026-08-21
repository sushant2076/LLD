from abc import ABC, abstractmethod

from rate_limiter.enums import RateLimitType
from rate_limiter.model import RateLimitConfig


class RateLimiter(ABC):
    """Strategy interface: every concrete rate limiting algorithm implements
    this contract so callers can swap algorithms interchangeably."""

    def __init__(self, config: RateLimitConfig, rate_limit_type: RateLimitType) -> None:
        self.config = config
        self.type = rate_limit_type

    @abstractmethod
    def allow_request(self, user_id: str) -> bool:
        """Return True if the request for user_id should be allowed."""
        raise NotImplementedError
