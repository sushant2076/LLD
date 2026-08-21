from rate_limiter.enums import RateLimitType
from rate_limiter.limiter import (
    FixedWindowRateLimiter,
    RateLimiter,
    SlidingWindowLogRateLimiter,
    TokenBucketRateLimiter,
)
from rate_limiter.model import RateLimitConfig


class RateLimiterFactory:
    """Selects and constructs the concrete rate limiter strategy for a
    given algorithm type."""

    @staticmethod
    def create_rate_limiter(
        algo: RateLimitType, config: RateLimitConfig
    ) -> RateLimiter:
        if algo == RateLimitType.TOKEN_BUCKET:
            return TokenBucketRateLimiter(config)
        if algo == RateLimitType.FIXED_WINDOW:
            return FixedWindowRateLimiter(config)
        if algo == RateLimitType.SLIDING_WINDOW_LOG:
            return SlidingWindowLogRateLimiter(config)
        raise ValueError(f"Unknown algorithm: {algo}")
