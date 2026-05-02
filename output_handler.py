import pandas as pd
import matplotlib.pyplot as plt

def generate_excel_report(trade_logs, performance_metrics, file_name='trade_report.xlsx'):
    """
    Generate an Excel report with trade logs and performance metrics.
    
    Parameters:
    - trade_logs (DataFrame): A DataFrame containing trade logs.
    - performance_metrics (dict): A dictionary containing performance metrics.
    - file_name (str): The name of the Excel file to generate.
    """
    with pd.ExcelWriter(file_name) as writer:
        trade_logs.to_excel(writer, sheet_name='Trade Logs', index=False)
        pd.DataFrame(performance_metrics).T.to_excel(writer, sheet_name='Performance Metrics')

def plot_trades(price_data, trades, filename='trade_plot.png'):
    """
    Create a plot showing price movements and trade points.
    
    Parameters:
    - price_data (DataFrame): A DataFrame containing price movements.
    - trades (DataFrame): A DataFrame containing trade points.
    - filename (str): The name of the file to save the plot.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(price_data['Date'], price_data['Price'], label='Price Movement', color='blue')
    
    for index, trade in trades.iterrows():
        plt.scatter(trade['Date'], trade['Price'], marker='o', color='red', label='Trade Point' if index == 0 else "")
    
    plt.title('Price Movement and Trade Points')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(filename)
    plt.close()

# Example usage
# trade_logs = pd.DataFrame(...)  # Replace with actual trade log DataFrame
# performance_metrics = {...}      # Replace with actual performance metrics
# price_data = pd.DataFrame(...)    # Replace with actual price data DataFrame
# trades = pd.DataFrame(...)         # Replace with actual trades DataFrame

# generate_excel_report(trade_logs, performance_metrics)
# plot_trades(price_data, trades)