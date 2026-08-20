from datetime import datetime

# Mirrors the Java pattern "d MMM h:mm a yyyy", e.g. "21 May 7:30 AM 2025"
_FORMAT = "%d %b %I:%M %p %Y"


class DateTimeParser:
    @staticmethod
    def parse(input_str: str) -> datetime:
        # datetime.strptime requires zero-padded day with %d; Java's "d" pattern
        # accepts single digits too, so normalize the leading day component.
        parts = input_str.split(maxsplit=1)
        if len(parts) == 2 and len(parts[0]) == 1:
            input_str = f"0{parts[0]} {parts[1]}"
        return datetime.strptime(input_str, _FORMAT)
