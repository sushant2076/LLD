from typing import TYPE_CHECKING

from examples.atm.enums.atm_status import ATMStatus
from examples.atm.model.card import Card
from examples.atm.state.atm_state import ATMState

if TYPE_CHECKING:
    from examples.atm.service.atm_machine import ATMMachine


class CardInsertedState(ATMState):
    """Card is in the machine; waiting for the PIN."""

    def __init__(self, atm_machine: "ATMMachine") -> None:
        self.atm_machine = atm_machine

    def insert_card(self, card: Card) -> None:
        print("Card already inserted.")

    def enter_pin(self, pin: str) -> None:
        from examples.atm.state.authenticated_state import AuthenticatedState

        current_card = self.atm_machine.current_card
        if current_card is not None and current_card.pin == pin:
            print("PIN correct. Authenticated.")
            self.atm_machine.set_state(AuthenticatedState(self.atm_machine))
        else:
            print("Invalid PIN.")

    def select_option(self, option: str) -> None:
        print("Enter PIN first.")

    def dispense_cash(self, amount: int) -> None:
        print("Enter PIN before dispensing.")

    def eject_card(self) -> None:
        from examples.atm.state.idle_state import IdleState

        self.atm_machine.current_card = None
        print("Card ejected.")
        self.atm_machine.set_state(IdleState(self.atm_machine))

    @property
    def status(self) -> ATMStatus:
        return ATMStatus.CARD_INSERTED
