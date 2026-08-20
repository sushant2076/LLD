"""Builds the handler chain and wires appenders to levels."""

from .appenders import LogAppender
from .enums import LogLevel
from .handlers import (
    DebugHandler,
    ErrorHandler,
    FatalHandler,
    InfoHandler,
    LogHandler,
    WarnHandler,
)


class LogHandlerConfiguration:
    _debug: LogHandler = DebugHandler()
    _info: LogHandler = InfoHandler()
    _warn: LogHandler = WarnHandler()
    _error: LogHandler = ErrorHandler()
    _fatal: LogHandler = FatalHandler()

    _level_to_handler = {
        LogLevel.DEBUG: _debug,
        LogLevel.INFO: _info,
        LogLevel.WARN: _warn,
        LogLevel.ERROR: _error,
        LogLevel.FATAL: _fatal,
    }

    @classmethod
    def build(cls) -> LogHandler:
        cls._debug.set_next(cls._info)
        cls._info.set_next(cls._warn)
        cls._warn.set_next(cls._error)
        cls._error.set_next(cls._fatal)
        return cls._debug

    @classmethod
    def add_appender_for_level(cls, level: LogLevel, appender: LogAppender) -> None:
        handler = cls._level_to_handler.get(level)
        if handler is None:
            raise ValueError(f"No handler configured for level {level}")
        handler.subscribe(appender)
