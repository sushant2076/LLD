import threading
import time
from typing import Dict

from rate_limiter.enums import RateLimitType
from rate_limiter.limiter.base import RateLimiter
from rate_limiter.model import RateLimitConfig


class TokenBucketRateLimiter(RateLimiter):
    """Token bucket algorithm: each user has a bucket of tokens that refills
    gradually over time; a request is allowed if a token is available."""

    def __init__(self, config: RateLimitConfig) -> None:
        super().__init__(config, RateLimitType.TOKEN_BUCKET)
        self._tokens: Dict[str, int] = {}
        self._last_refill_time: Dict[str, float] = {}
        # Java's ConcurrentHashMap.compute() gives per-key atomic
        # read-modify-write semantics; a single lock reproduces that here.
        self._lock = threading.Lock()

    def allow_request(self, user_id: str) -> bool:
        now = time.time() * 1000  # milliseconds, mirrors System.currentTimeMillis()

        with self._lock:
            current_tokens = self._refill_tokens(user_id, now)

            if current_tokens > 0:
                self._tokens[user_id] = current_tokens - 1
                return True

            self._tokens[user_id] = current_tokens
            return False

    def _refill_tokens(self, user_id: str, now: float) -> int:
        refill_rate = self.config.window_in_seconds / self.config.max_requests

        self._last_refill_time.setdefault(user_id, now)
        last_refill = self._last_refill_time[user_id]

        elapsed_seconds = (now - last_refill) / 1000
        refill_tokens = int(elapsed_seconds / refill_rate)
        current_tokens = self._tokens.get(user_id, self.config.max_requests)
        current_tokens = min(self.config.max_requests, current_tokens + refill_tokens)

        if refill_tokens > 0:
            self._last_refill_time[user_id] = now

        return current_tokens
