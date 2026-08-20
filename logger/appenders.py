"""Appenders (sinks) that write formatted log messages somewhere."""

import threading
from abc import ABC, abstractmethod

from .formatter import LogFormatter
from .model import LogMessage


class LogAppender(ABC):
    @abstractmethod
    def append(self, message: LogMessage) -> None:
        raise NotImplementedError


class ConsoleAppender(LogAppender):
    def __init__(self, formatter: LogFormatter):
        self._formatter = formatter

    def append(self, message: LogMessage) -> None:
        print(self._formatter.format(message))


class FileAppender(LogAppender):
    def __init__(self, formatter: LogFormatter, file_name: str):
        self._formatter = formatter
        self._lock = threading.Lock()
        try:
            self._file = open(file_name, "a", encoding="utf-8")
        except OSError as exc:
            raise RuntimeError("Failed to open log file") from exc

    def append(self, message: LogMessage) -> None:
        with self._lock:
            try:
                self._file.write(self._formatter.format(message))
                self._file.write("\n")
                self._file.flush()
            except OSError as exc:
                print(f"Failed to write log message: {exc}")

    def close(self) -> None:
        with self._lock:
            self._file.close()
