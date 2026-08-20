from datetime import time


def convert_string_to_local_time(value: str) -> time:
    """Convert a "H:MM" formatted string into a datetime.time object."""
    hour_str, minute_str = value.split(":")
    return time(hour=int(hour_str), minute=int(minute_str))
