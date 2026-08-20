from ..enums.pricing_strategy_type import PricingStrategyType
from ..strategy.pricing.event_based_pricing import EventBasedPricing
from ..strategy.pricing.pricing_strategy import PricingStrategy
from ..strategy.pricing.time_based_pricing import TimeBasedPricing

_CREATORS = {
    PricingStrategyType.TIME_BASED: TimeBasedPricing,
    PricingStrategyType.EVENT_BASED: EventBasedPricing,
}


class PricingStrategyFactory:
    """Mirrors PricingStrategyFactory.java."""

    @staticmethod
    def get(strategy_type: PricingStrategyType) -> PricingStrategy:
        try:
            cls = _CREATORS[strategy_type]
        except KeyError as exc:
            raise ValueError(f"Unsupported pricing strategy type: {strategy_type}") from exc
        return cls()
