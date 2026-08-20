"""Strategy pattern: pluggable formatters for log messages."""

from abc import ABC, abstractmethod
from datetime import datetime

from .model import LogMessage

_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class LogFormatter(ABC):
    @abstractmethod
    def format(self, message: LogMessage) -> str:
        raise NotImplementedError


class PlainTextFormatter(LogFormatter):
    def format(self, message: LogMessage) -> str:
        formatted_time = datetime.fromtimestamp(
            message.timestamp / 1000.0
        ).strftime(_TIME_FORMAT)
        return f"{formatted_time} [{message.level}] - {message.message}"


class JsonFormatter(LogFormatter):
    def format(self, message: LogMessage) -> str:
        formatted_time = datetime.fromtimestamp(
            message.timestamp / 1000.0
        ).strftime(_TIME_FORMAT)
        return (
            '{"timestamp": "%s", "level": "%s", "message": "%s"}'
            % (formatted_time, message.level, message.message)
        )
