"""A small, dependency-free logging framework ported from a Java LLD example.

Demonstrates:
- Strategy pattern (LogFormatter implementations)
- Chain of Responsibility (LogHandler subclasses per level)
- Observer-ish fan-out (LogAppender subscribers per handler)
- Singleton (Logger)
"""

from .appenders import ConsoleAppender, FileAppender, LogAppender
from .config import LogHandlerConfiguration
from .enums import LogLevel
from .formatter import JsonFormatter, LogFormatter, PlainTextFormatter
from .handlers import (
    DebugHandler,
    ErrorHandler,
    FatalHandler,
    InfoHandler,
    LogHandler,
    WarnHandler,
)
from .logger import Logger
from .model import LogMessage

__all__ = [
    "ConsoleAppender",
    "FileAppender",
    "LogAppender",
    "LogHandlerConfiguration",
    "LogLevel",
    "JsonFormatter",
    "LogFormatter",
    "PlainTextFormatter",
    "DebugHandler",
    "ErrorHandler",
    "FatalHandler",
    "InfoHandler",
    "LogHandler",
    "WarnHandler",
    "Logger",
    "LogMessage",
]
