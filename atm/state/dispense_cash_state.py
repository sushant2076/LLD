from typing import TYPE_CHECKING

from examples.atm.cor.cash_dispenser_chain_builder import CashDispenserChainBuilder
from examples.atm.enums.atm_status import ATMStatus
from examples.atm.model.card import Card
from examples.atm.state.atm_state import ATMState

if TYPE_CHECKING:
    from examples.atm.service.atm_machine import ATMMachine


class DispenseCashState(ATMState):
    """Option selected; ready to validate and dispense cash."""

    def __init__(self, atm_machine: "ATMMachine") -> None:
        self.atm_machine = atm_machine
        self.chain = CashDispenserChainBuilder.build_chain()

    def insert_card(self, card: Card) -> None:
        print("Transaction in progress. Cannot insert another card.")

    def enter_pin(self, pin: str) -> None:
        print("Already authenticated.")

    def select_option(self, option: str) -> None:
        print("Option already selected.")

    def dispense_cash(self, amount: int) -> None:
        atm = self.atm_machine.atm
        card = self.atm_machine.current_card
        assert card is not None

        atm_balance = atm.cash_available
        account_balance = card.account.balance

        if amount > atm_balance:
            print(f"ATM has insufficient cash. Cannot dispense {amount}")
            self.eject_card()
            return

        if amount > account_balance:
            print("Insufficient account balance.")
            self.eject_card()
            return

        # Now check if note combination is possible
        if self.chain.can_dispense(atm, amount):
            self.chain.dispense(atm, amount)

            # Deduct from ATM cash & account balance
            atm.cash_available = atm_balance - amount
            card.account.balance = account_balance - amount

            self.eject_card()
            print(f"Cash dispensed: {amount}")
        else:
            print("Cannot dispense requested amount with available denominations.")
            self.eject_card()

    def eject_card(self) -> None:
        from examples.atm.state.idle_state import IdleState

        self.atm_machine.current_card = None
        print("Card ejected.")
        self.atm_machine.set_state(IdleState(self.atm_machine))  # use factory

    @property
    def status(self) -> ATMStatus:
        return ATMStatus.DISPENSE_CASH
