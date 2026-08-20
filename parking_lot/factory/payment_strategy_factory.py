from ..enums.payment_mode import PaymentMode
from ..strategy.payment.card_payment import CardPayment
from ..strategy.payment.cash_payment import CashPayment
from ..strategy.payment.payment_strategy import PaymentStrategy
from ..strategy.payment.upi_payment import UpiPayment

_CREATORS = {
    PaymentMode.CASH: CashPayment,
    PaymentMode.UPI: UpiPayment,
    PaymentMode.CARD: CardPayment,
}


class PaymentStrategyFactory:
    """Mirrors PaymentStrategyFactory.java."""

    @staticmethod
    def get(mode: PaymentMode) -> PaymentStrategy:
        try:
            cls = _CREATORS[mode]
        except KeyError as exc:
            raise ValueError(f"Unsupported payment mode: {mode}") from exc
        return cls()
