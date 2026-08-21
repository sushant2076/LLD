from atm.enums.atm_status import ATMStatus


class ATM:
    """Physical ATM machine state: cash inventory and current status."""

    def __init__(
        self,
        id: str,
        two_thousand_count: int,
        five_hundred_count: int,
        one_hundred_count: int,
    ) -> None:
        self.id = id
        self.cash_available: float = (
            2000 * two_thousand_count
            + 500 * five_hundred_count
            + 100 * one_hundred_count
        )
        self.status: ATMStatus = ATMStatus.IDLE
        self.two_thousand_count = two_thousand_count
        self.five_hundred_count = five_hundred_count
        self.one_hundred_count = one_hundred_count
