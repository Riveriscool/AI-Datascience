import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read the Excel file
df = pd.read_excel('/Users/riverwalser/Physics/AMZN (4).xlsx')

# Calculate the 10-day moving average
window = 10
df['Moving Average'] = df['Adj Close'].rolling(window=window).mean()

# Plot the scatter plot
fig, ax = plt.subplots()
ax.scatter(df['Moving Average'], df['Adj Close'])

# Customize the plot
ax.set_xlabel('10-day Moving Average')
ax.set_ylabel('Adjusted Close')
ax.set_title('Amazon Stock: 10-day Moving Average vs Adjusted Close')

# Save the scatterplot data to an Excel file
scatterplot_data = pd.DataFrame({'Moving Average': df['Moving Average'], 'Adj Close': df['Adj Close']})
scatterplot_data.to_excel('scatterplot_data.xlsx', index=False)

# Display the plot
plt.show()

# Drop rows with NaN values
df = df.dropna(subset=['Moving Average', 'Adj Close'])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(df['Moving Average'], df['Adj Close'])

# Plot the scatter plot with regression line
fig, ax = plt.subplots()
ax.scatter(df['Moving Average'], df['Adj Close'], label='Data')

# Create the regression line
x_vals = df['Moving Average']
y_vals = intercept + slope * x_vals
ax.plot(x_vals, y_vals, color='red', label='Regression Line')

# Customize the plot
ax.set_xlabel('10-day Moving Average')
ax.set_ylabel('Adjusted Close')
ax.set_title('Linear Regression: Moving Average vs Adjusted Close')
ax.legend()

# Display the plot
plt.show()

# Print the coefficients and R-squared value
print("Coefficients:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value**2)
previous_rolling_avg = 1000

# Predict the stock closing price
predicted_close = intercept + slope * previous_rolling_avg

# Print the predicted closing price
print("Predicted Closing Price:", predicted_close)