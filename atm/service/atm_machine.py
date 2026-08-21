from typing import Optional

from atm.factory.atm_state_factory import ATMStateFactory
from atm.model.atm import ATM
from atm.model.card import Card
from atm.repository.atm_repository import ATMRepository
from atm.state.atm_state import ATMState


class ATMMachine:
    """Context class for the State pattern; delegates all operations to the
    current ATMState and transitions between states."""

    def __init__(self, atm_id: str, atm_repository: ATMRepository) -> None:
        self.atm_repository = atm_repository
        atm: Optional[ATM] = atm_repository.get_by_id(atm_id)
        if atm is None:
            raise RuntimeError("ATM not found")
        self.atm: ATM = atm
        self.current_card: Optional[Card] = None
        self.state: ATMState = ATMStateFactory.get_state(self.atm.status, self)

    def insert_card(self, card: Card) -> None:
        self.state.insert_card(card)

    def enter_pin(self, pin: str) -> None:
        self.state.enter_pin(pin)

    def select_option(self, option: str) -> None:
        self.state.select_option(option)

    def dispense_cash(self, amount: int) -> None:
        self.state.dispense_cash(amount)

    def eject_card(self) -> None:
        self.state.eject_card()

    def set_state(self, state: ATMState) -> None:
        self.state = state
        self.atm.status = state.status
        # persist the changes in db
