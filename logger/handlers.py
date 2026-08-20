"""Chain of Responsibility: one handler per log level.

Each handler decides whether it can handle a given LogMessage's level; if
not, it forwards the message to the next handler in the chain. When a
handler can handle a message, it notifies all its subscribed appenders
(a simple Observer pattern).
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from .appenders import LogAppender
from .enums import LogLevel
from .model import LogMessage


class LogHandler(ABC):
    def __init__(self) -> None:
        self.next: Optional["LogHandler"] = None
        self._appenders: List[LogAppender] = []

    def set_next(self, next_handler: "LogHandler") -> None:
        self.next = next_handler

    def subscribe(self, appender: LogAppender) -> None:
        self._appenders.append(appender)

    def notify_observers(self, message: LogMessage) -> None:
        for appender in self._appenders:
            appender.append(message)

    def handle(self, message: LogMessage) -> None:
        if self.can_handle(message.level):
            self.notify_observers(message)
        elif self.next is not None:
            self.next.handle(message)

    @abstractmethod
    def can_handle(self, level: LogLevel) -> bool:
        raise NotImplementedError


class DebugHandler(LogHandler):
    def can_handle(self, level: LogLevel) -> bool:
        return level == LogLevel.DEBUG


class InfoHandler(LogHandler):
    def can_handle(self, level: LogLevel) -> bool:
        return level == LogLevel.INFO


class WarnHandler(LogHandler):
    def can_handle(self, level: LogLevel) -> bool:
        return level == LogLevel.WARN


class ErrorHandler(LogHandler):
    def can_handle(self, level: LogLevel) -> bool:
        return level == LogLevel.ERROR


class FatalHandler(LogHandler):
    def can_handle(self, level: LogLevel) -> bool:
        return level == LogLevel.FATAL
