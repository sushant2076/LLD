"""Singleton Logger facade over the handler chain."""

import time

from .config import LogHandlerConfiguration
from .enums import LogLevel
from .model import LogMessage


class Logger:
    _instance: "Logger" = None

    def __init__(self) -> None:
        if Logger._instance is not None:
            raise RuntimeError("Logger is a singleton; use Logger.get_instance()")
        self._handler_chain = LogHandlerConfiguration.build()

    @classmethod
    def get_instance(cls) -> "Logger":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def log(self, level: LogLevel, message: str) -> None:
        msg = LogMessage(level, message, int(time.time() * 1000))
        self._handler_chain.handle(msg)

    def trace(self, message: str) -> None:
        self.log(LogLevel.TRACE, message)

    def debug(self, message: str) -> None:
        self.log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        self.log(LogLevel.INFO, message)

    def warn(self, message: str) -> None:
        self.log(LogLevel.WARN, message)

    def error(self, message: str) -> None:
        self.log(LogLevel.ERROR, message)

    def fatal(self, message: str) -> None:
        self.log(LogLevel.FATAL, message)
