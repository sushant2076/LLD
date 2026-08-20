import threading
import time
from collections import deque
from typing import Deque, Dict

from examples.rate_limiter.enums import RateLimitType
from examples.rate_limiter.limiter.base import RateLimiter
from examples.rate_limiter.model import RateLimitConfig


class SlidingWindowLogRateLimiter(RateLimiter):
    """Sliding window log algorithm: keeps a timestamp log per user and
    counts how many requests fall within the trailing window."""

    def __init__(self, config: RateLimitConfig) -> None:
        super().__init__(config, RateLimitType.SLIDING_WINDOW_LOG)
        self._request_log: Dict[str, Deque[int]] = {}
        self._lock = threading.Lock()

    def allow_request(self, user_id: str) -> bool:
        now = int(time.time())

        with self._lock:
            log = self._request_log.setdefault(user_id, deque())

            while log and (now - log[0]) >= self.config.window_in_seconds:
                log.popleft()

            if len(log) < self.config.max_requests:
                log.append(now)
                return True

            return False
