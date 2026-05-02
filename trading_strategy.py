class TradingStrategy:
    def __init__(self):
        self.buy_signal = -0.15  # Buy signal for a -15% drop
        self.sell_signal = 0.20  # Sell signal for a +20% profit
        self.position = 0  # Track the current position (0 = no position, 1 = long)

    def check_buy_signal(self, current_price, previous_price):
        if (previous_price - current_price) / previous_price >= self.buy_signal:
            self.position = 1  # Buy
            return 'Buy Signal'
        return 'No Buy Signal'

    def check_sell_signal(self, current_price, purchase_price):
        if (current_price - purchase_price) / purchase_price >= self.sell_signal:
            self.position = 0  # Sell
            return 'Sell Signal'
        return 'No Sell Signal'  

# Example usage
# strategy = TradingStrategy()
# print(strategy.check_buy_signal(current_price, previous_price))
# print(strategy.check_sell_signal(current_price, purchase_price))
