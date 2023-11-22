import pandas as pd
import matplotlib.pyplot as plt

file_path = "./google.csv"

# Column names for the CSV file without a header row
column_names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

google_stock = pd.read_csv(file_path, names=column_names, parse_dates=['Date'], index_col='Date')
# Sort the data by date for chronological order
google_stock.sort_index(inplace=True)

# Plotting the closing prices
# Creates a plot with specified dimensions (10 inches wide, 6 inches tall)
plt.figure(figsize=(10, 6))  
# Plots the 'Close' column from the DataFrame, which represents the closing price of the stock. Adds a label for the legend.
plt.plot(google_stock['Close'], label='Closing Price')  
# Labels
plt.xlabel('Date')  
plt.ylabel('Price (USD)')  
plt.title('Google Stock Closing Prices in 2014')  
plt.legend() 
plt.grid(True)  
# Displays the plot
plt.show()  
