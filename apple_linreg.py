import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Read the data from Excel file
df = pd.read_excel('/Users/riverwalser/Physics/AMZN (4).xlsx')

# Filter out rows with zero values
df = df[(df['APPL AVERAGE MOVEMENT'] != 0) & (df['AVG MOVEMENT'] != 0)]

# Extract the data for x-axis and y-axis
x_values = df['APPL AVERAGE MOVEMENT']
y_values = df['AVG MOVEMENT']

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)

# Calculate the regression line
regression_line = slope * x_values + intercept

# Create the graph
plt.plot(x_values, y_values, 'o', label='Data')
plt.plot(x_values, regression_line, 'r-', label='Regression Line')
plt.xlabel('APPL AVERAGE MOVEMENT')
plt.ylabel('AVG MOVEMENT')
plt.title('Graph of APPL AVERAGE MOVEMENT vs. AVG MOVEMENT')

# Add the regression equation to the plot
equation_text = f'Regression Line: y = {slope:.2f}x + {intercept:.2f}\nR-value: {r_value:.2f}'
plt.text(0.1, 0.9, equation_text, transform=plt.gca().transAxes)

# Show the legend
plt.legend()

# Show the graph
plt.show()
