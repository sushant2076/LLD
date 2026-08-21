from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, entry_time, exit_time):
        pass