from enums.pricing import PricingEnum
from strategy.time_based_pricing import TimeBasedPricing

_CATEGORY = {
    PricingEnum.TIMING: TimeBasedPricing,
}

class PricingFactory:
    @staticmethod
    def get(pricing_strategy: PricingEnum):
        return _CATEGORY[pricing_strategy]
        