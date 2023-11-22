import pandas as pd
import matplotlib.pyplot as plt


file_path = 'path_to_your_file/google.csv'

# Read the CSV file
google_stock = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

# Sort the data by date just in case
google_stock.sort_index(inplace=True)

# Plotting the closing prices
# Creates plot (10 inches wide, 6 inches tall).
plt.figure(figsize=(10, 6))  
# Plots the 'Close' column from the DataFrame, which represents the closing price of the stock. The label is used for the legend.
plt.plot(google_stock['Close'], label='Closing Price')  
# Labels
plt.xlabel('Date')  
plt.ylabel('Price (USD)')  
plt.title('Google Stock Closing Prices in 2014')  
plt.legend() 
# Enables the grid for better readability of the plot.
plt.grid(True)  

plt.show()  
