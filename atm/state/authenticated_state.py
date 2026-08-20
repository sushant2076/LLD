from typing import TYPE_CHECKING

from examples.atm.enums.atm_status import ATMStatus
from examples.atm.model.card import Card
from examples.atm.state.atm_state import ATMState

if TYPE_CHECKING:
    from examples.atm.service.atm_machine import ATMMachine


class AuthenticatedState(ATMState):
    """PIN verified; waiting for the customer to pick an option."""

    def __init__(self, atm_machine: "ATMMachine") -> None:
        self.atm_machine = atm_machine

    def insert_card(self, card: Card) -> None:
        print("Card already inserted.")

    def enter_pin(self, pin: str) -> None:
        print("Already authenticated.")

    def select_option(self, option: str) -> None:
        # Could add options like deposit, check balance based on option selected.
        from examples.atm.state.dispense_cash_state import DispenseCashState

        print("Option selected: Withdrawal.")
        self.atm_machine.set_state(DispenseCashState(self.atm_machine))

    def dispense_cash(self, amount: int) -> None:
        print("Select an option first.")

    def eject_card(self) -> None:
        from examples.atm.state.idle_state import IdleState

        self.atm_machine.current_card = None
        print("Card ejected.")
        self.atm_machine.set_state(IdleState(self.atm_machine))

    @property
    def status(self) -> ATMStatus:
        return ATMStatus.AUTHENTICATED
