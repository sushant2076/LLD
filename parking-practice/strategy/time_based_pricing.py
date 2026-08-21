from strategy.pricing_strategy import PricingStrategy


class TimeBasedPricing(PricingStrategy):
    def calculate_fee(self, entry_time, exit_time):
        return (exit_time-entry_time)/60 * 100;