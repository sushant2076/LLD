"""Data model for a single log message."""

from dataclasses import dataclass

from .enums import LogLevel


@dataclass(frozen=True)
class LogMessage:
    level: LogLevel
    message: str
    timestamp: int
