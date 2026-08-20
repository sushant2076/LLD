"""Generic rate limiter LLD example.

Ported from the Java example at
org.nailyourinterview.lld.rate_limiter (Low-Level-Design repo).

Demonstrates the Strategy pattern for pluggable rate limiting algorithms
(token bucket, fixed window, sliding window log) selected per user tier
via a factory.
"""
