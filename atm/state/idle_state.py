from typing import TYPE_CHECKING

from atm.enums.atm_status import ATMStatus
from atm.model.card import Card
from atm.state.atm_state import ATMState

if TYPE_CHECKING:
    from atm.service.atm_machine import ATMMachine


class IdleState(ATMState):
    """No card inserted; machine is waiting."""

    def __init__(self, atm_machine: "ATMMachine") -> None:
        self.atm_machine = atm_machine

    def insert_card(self, card: Card) -> None:
        # Local import to avoid a circular import with card_inserted_state.
        from atm.state.card_inserted_state import CardInsertedState

        self.atm_machine.current_card = card
        print("Card inserted.")
        self.atm_machine.set_state(CardInsertedState(self.atm_machine))

    def enter_pin(self, pin: str) -> None:
        print("No card inserted.")

    def select_option(self, option: str) -> None:
        print("No card inserted.")

    def dispense_cash(self, amount: int) -> None:
        print("No card inserted.")

    def eject_card(self) -> None:
        print("No card to eject.")

    @property
    def status(self) -> ATMStatus:
        return ATMStatus.IDLE
