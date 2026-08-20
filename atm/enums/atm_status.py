from enum import Enum, auto


class ATMStatus(Enum):
    IDLE = auto()
    CARD_INSERTED = auto()
    AUTHENTICATED = auto()
    DISPENSE_CASH = auto()
