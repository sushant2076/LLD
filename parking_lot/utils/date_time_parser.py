from datetime import datetime

# Java pattern "d MMM h:mm a yyyy" -> Python strptime equivalent.
_FORMAT = "%d %b %I:%M %p %Y"


class DateTimeParser:
    """Mirrors DateTimeParser.java."""

    @staticmethod
    def parse(input_str: str) -> datetime:
        return datetime.strptime(input_str, _FORMAT)
