import threading
import time
from typing import Dict

from rate_limiter.enums import RateLimitType
from rate_limiter.limiter.base import RateLimiter
from rate_limiter.model import RateLimitConfig


class FixedWindowRateLimiter(RateLimiter):
    """Fixed window algorithm: time is divided into fixed-size windows; each
    user may make at most max_requests requests within the current window."""

    def __init__(self, config: RateLimitConfig) -> None:
        super().__init__(config, RateLimitType.FIXED_WINDOW)
        self._request_count: Dict[str, int] = {}
        self._window_start: Dict[str, int] = {}
        self._lock = threading.Lock()

    def allow_request(self, user_id: str) -> bool:
        current_req_window = int(time.time()) // self.config.window_in_seconds

        with self._lock:
            last_req_window = self._window_start.get(user_id, current_req_window)

            if last_req_window != current_req_window:
                # window expired -> reset counter and window of last req
                self._window_start[user_id] = current_req_window
                self._request_count[user_id] = 1
                return True

            count = self._request_count.get(user_id, 0)

            if count < self.config.max_requests:
                self._request_count[user_id] = count + 1
                return True

            return False
