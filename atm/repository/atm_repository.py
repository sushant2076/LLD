from typing import Dict, Optional

from examples.atm.enums.atm_status import ATMStatus
from examples.atm.model.atm import ATM


class ATMRepository:
    """In-memory store of ATM machines, keyed by id."""

    def __init__(self) -> None:
        self._atms: Dict[str, ATM] = {}

    def save(self, atm: ATM) -> None:
        self._atms[atm.id] = atm

    def get_by_id(self, id: str) -> Optional[ATM]:
        return self._atms.get(id)

    def update_atm_status_by_id(self, id: str, new_status: ATMStatus) -> None:
        atm = self._atms[id]
        atm.status = new_status
