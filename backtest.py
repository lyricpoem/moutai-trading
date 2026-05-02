class Backtest:
    def __init__(self, initial_capital):
        self.initial_capital = initial_capital
        self.trades = []
        self.current_capital = initial_capital
        self.annual_returns = []

    def record_trade(self, entry_price, exit_price, shares):
        trade_result = (exit_price - entry_price) * shares
        self.trades.append(trade_result)
        self.current_capital += trade_result

    def calculate_annual_returns(self):
        total_return = self.current_capital - self.initial_capital
        annual_return = (total_return / self.initial_capital) * 100
        return annual_return

    def generate_performance_metrics(self):
        total_trades = len(self.trades)
        win_trades = len([t for t in self.trades if t > 0])
        loss_trades = total_trades - win_trades
        win_ratio = win_trades / total_trades if total_trades > 0 else 0
        total_return = self.current_capital - self.initial_capital

        metrics = {
            'Total Trades': total_trades,
            'Winning Trades': win_trades,
            'Losing Trades': loss_trades,
            'Win Ratio': win_ratio,
            'Total Return': total_return,
            'Current Capital': self.current_capital,
            'Annual Return (%)': self.calculate_annual_returns(),
        }
        return metrics

# Example Usage:
if __name__ == '__main__':
    backtest = Backtest(initial_capital=1000000)
    # Simulating trades (replace with actual trading logic)
    backtest.record_trade(100, 110, 10)
    backtest.record_trade(110, 100, 10)
    performance = backtest.generate_performance_metrics()
    print(performance) 
