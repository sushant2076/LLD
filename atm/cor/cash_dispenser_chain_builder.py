from examples.atm.cor.cash_dispenser import CashDispenser
from examples.atm.cor.five_hundred_dispenser import FiveHundredDispenser
from examples.atm.cor.one_hundred_dispenser import OneHundredDispenser
from examples.atm.cor.two_thousand_dispenser import TwoThousandDispenser


class CashDispenserChainBuilder:
    """Builds the ₹2000 -> ₹500 -> ₹100 chain of responsibility."""

    @staticmethod
    def build_chain() -> CashDispenser:
        d1: CashDispenser = TwoThousandDispenser()
        d2: CashDispenser = FiveHundredDispenser()
        d3: CashDispenser = OneHundredDispenser()

        d1.set_next_dispenser(d2)
        d2.set_next_dispenser(d3)
        return d1
