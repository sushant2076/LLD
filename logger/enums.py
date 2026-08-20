"""Log level definitions for the logging framework."""

from enum import Enum, auto


class LogLevel(Enum):
    TRACE = auto()
    DEBUG = auto()
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    FATAL = auto()

    def __str__(self) -> str:
        return self.name
