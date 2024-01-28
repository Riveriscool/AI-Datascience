import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Read the Excel file
df = pd.read_excel('AMZN (4).xlsx')

# Calculate the 10-day momentum
df['10-day Momentum'] = df['Close'].diff(10)

# Calculate the 10-day rolling average
df['10-day Rolling Avg'] = df['Close'].rolling(window=10).mean()

# Shift the Avg Movement category one row down
df['AVG MOVEMENT'] = df['AVG MOVEMENT'].shift(-1)

# Drop the last row with NaN Avg Movement
df = df.dropna(subset=['AVG MOVEMENT'])

# Plot the scatter plot
fig, ax = plt.subplots()
colors = {'Up': 'green', 'Down': 'red'}
ax.scatter(df['10-day Momentum'], df['10-day Rolling Avg'], c=df['AVG MOVEMENTpiip'].map(colors))

# Customize the plot
ax.set_xlabel('10-day Momentum')
ax.set_ylabel('10-day Rolling Average')
ax.set_title('Stock Movement: 10-day Momentum vs 10-day Rolling Average')

# Split the data into training and testing sets
X = df[['10-day Momentum', '10-day Rolling Avg']]
y = df['Avg Movement']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Display the plot
plt.show()
