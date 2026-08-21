from typing import TYPE_CHECKING

from atm.enums.atm_status import ATMStatus
from atm.state.atm_state import ATMState
from atm.state.authenticated_state import AuthenticatedState
from atm.state.card_inserted_state import CardInsertedState
from atm.state.dispense_cash_state import DispenseCashState
from atm.state.idle_state import IdleState

if TYPE_CHECKING:
    from atm.service.atm_machine import ATMMachine


class ATMStateFactory:
    """Factory that maps an ATMStatus to its concrete ATMState instance."""

    @staticmethod
    def get_state(status: ATMStatus, machine: "ATMMachine") -> ATMState:
        if status == ATMStatus.IDLE:
            return IdleState(machine)
        if status == ATMStatus.CARD_INSERTED:
            return CardInsertedState(machine)
        if status == ATMStatus.AUTHENTICATED:
            return AuthenticatedState(machine)
        if status == ATMStatus.DISPENSE_CASH:
            return DispenseCashState(machine)
        raise ValueError(f"Unknown ATM status: {status}")
