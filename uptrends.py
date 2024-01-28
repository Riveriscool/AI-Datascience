import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('/Users/riverwalser/Physics/AMZN (4).xlsx')

# Specify the column name for the adjusted close prices
adj_close_column = 'Adj Close'

# Get the adjusted close prices
prices = df[adj_close_column].tolist()

# Create an empty matrix to store the uptrend indices
uptrend_matrix = []

# Identify uptrends
uptrend = []
for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        uptrend.append(i)
    else:
        if len(uptrend) >= 4:
            uptrend_matrix.append(uptrend)
        uptrend = []

# Plot the data
fig, ax = plt.subplots()

# Plot the entire dataset
ax.plot(df['Date'], prices, color='blue')

# Highlight uptrend areas with more opaque red dashed lines
for uptrend in uptrend_matrix:
    x = df['Date'].iloc[uptrend]
    y = df[adj_close_column].iloc[uptrend]
    ax.plot(x, y, color='red', linestyle='dashed', linewidth=3)

# Customize the plot
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Amazon Stock Price with Uptrend Highlighting')

# Rotate x-axis labels for better readability
fig.autofmt_xdate()

# Display the plot
plt.show()
