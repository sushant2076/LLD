from abc import ABC, abstractmethod

from ..enums.gate_type import GateType


class Gate(ABC):
    """Mirrors Gate.java (Lombok @Getter @AllArgsConstructor abstract class)."""

    def __init__(self, id: str):
        self.id = id

    @property
    @abstractmethod
    def type(self) -> GateType:
        raise NotImplementedError
