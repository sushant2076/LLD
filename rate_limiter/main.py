import threading
import time

from examples.rate_limiter.enums import RateLimitType, UserTier
from examples.rate_limiter.factory import RateLimiterFactory
from examples.rate_limiter.model import RateLimitConfig, User
from examples.rate_limiter.service import RateLimiterService


def check_concurrency(rate_limiter_service: RateLimiterService) -> None:
    """Fire 20 concurrent requests for the same free-tier user, mirroring
    the CyclicBarrier + CountDownLatch based test in the Java Main class."""
    free_user1 = User("user1", UserTier.FREE)

    threads = 20
    barrier = threading.Barrier(threads)
    results = [None] * threads

    def worker(req_num: int) -> None:
        barrier.wait()  # all threads wait here until barrier is full
        allowed = rate_limiter_service.allow_request(free_user1)
        results[req_num - 1] = (
            f"{threading.current_thread().name} | Request {req_num} for "
            f"FreeUser1: {'ALLOWED' if allowed else 'BLOCKED'}"
        )

    thread_list = [
        threading.Thread(target=worker, args=(i,), name=f"Thread-{i}")
        for i in range(1, threads + 1)
    ]
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()

    for line in results:
        print(line)


def demo_sequential_requests(rate_limiter_service: RateLimiterService) -> None:
    free_user = User("user1", UserTier.FREE)  # 10 req in 60 sec
    premium_user = User("user2", UserTier.PREMIUM)  # 100 req in 60 sec

    print("=== Free User Requests (Token Bucket) ===")
    for i in range(1, 16):
        allowed = rate_limiter_service.allow_request(free_user)
        print(f"Request {i} for Free User: {'ALLOWED' if allowed else 'BLOCKED'}")
        time.sleep(0.05)

    print("\n=== Premium User Requests (Fixed Window) ===")
    for i in range(1, 16):
        allowed = rate_limiter_service.allow_request(premium_user)
        print(f"Request {i} for Premium User: {'ALLOWED' if allowed else 'BLOCKED'}")
        time.sleep(0.05)


def demo_sliding_window_log() -> None:
    print("\n=== Sliding Window Log Requests ===")
    limiter = RateLimiterFactory.create_rate_limiter(
        RateLimitType.SLIDING_WINDOW_LOG,
        RateLimitConfig(max_requests=5, window_in_seconds=2),
    )
    user_id = "user3"
    for i in range(1, 8):
        allowed = limiter.allow_request(user_id)
        print(f"Request {i}: {'ALLOWED' if allowed else 'BLOCKED'}")
        time.sleep(0.1)


def main() -> None:
    rate_limiter_service = RateLimiterService()

    demo_sequential_requests(rate_limiter_service)
    demo_sliding_window_log()

    print("\n=== Concurrency Check (20 simultaneous requests) ===")
    check_concurrency(rate_limiter_service)


if __name__ == "__main__":
    main()
