from typing import Dict

from examples.rate_limiter.enums import RateLimitType, UserTier
from examples.rate_limiter.factory import RateLimiterFactory
from examples.rate_limiter.limiter import RateLimiter
from examples.rate_limiter.model import RateLimitConfig, User


class RateLimiterService:
    """Configures a rate limiting strategy per user tier and dispatches
    requests to the appropriate limiter."""

    def __init__(self) -> None:
        self._rate_limiters: Dict[UserTier, RateLimiter] = {}

        # Configure per-tier limits + algorithms
        self._rate_limiters[UserTier.FREE] = RateLimiterFactory.create_rate_limiter(
            RateLimitType.TOKEN_BUCKET,
            RateLimitConfig(max_requests=10, window_in_seconds=60),  # 10 req/min
        )

        self._rate_limiters[UserTier.PREMIUM] = RateLimiterFactory.create_rate_limiter(
            RateLimitType.FIXED_WINDOW,
            RateLimitConfig(max_requests=100, window_in_seconds=60),  # 100 req/min
        )

    def allow_request(self, user: User) -> bool:
        limiter = self._rate_limiters.get(user.tier)
        if limiter is None:
            raise ValueError(f"No limiter configured for tier: {user.tier}")
        return limiter.allow_request(user.user_id)
