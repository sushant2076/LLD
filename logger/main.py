"""Demo entry point exercising the logging framework, mirroring the
original Java Main class."""

import os

from .appenders import ConsoleAppender, FileAppender
from .config import LogHandlerConfiguration
from .enums import LogLevel
from .formatter import PlainTextFormatter
from .logger import Logger


def main() -> None:
    logger = Logger.get_instance()

    log_file = os.path.join(os.path.dirname(__file__), "logs.txt")

    LogHandlerConfiguration.add_appender_for_level(
        LogLevel.INFO,
        ConsoleAppender(PlainTextFormatter()),
    )

    LogHandlerConfiguration.add_appender_for_level(
        LogLevel.ERROR,
        ConsoleAppender(PlainTextFormatter()),
    )

    file_appender = FileAppender(PlainTextFormatter(), log_file)
    LogHandlerConfiguration.add_appender_for_level(
        LogLevel.ERROR,
        file_appender,
    )

    # Usage
    logger.debug("This debug message has no appenders, so it is silently dropped")
    logger.info("This is some key information")  # CONSOLE
    logger.warn("This warning has no appenders, so it is silently dropped")
    logger.error("Oh no! there's an error")  # CONSOLE + FILE
    logger.fatal("This fatal message has no appenders, so it is silently dropped")

    file_appender.close()


if __name__ == "__main__":
    main()
