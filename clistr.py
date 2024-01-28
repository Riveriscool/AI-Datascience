import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('ipenis.xlsx')

# Get unique categories
categories = df.iloc[:, 3].unique()

# Calculate average sentiment for each category
category_sentiments = {}
for category in categories:
    category_df = df[df.iloc[:, 3] == category]
    average_sentiment = category_df.iloc[:, 6].mean()
    category_sentiments[category] = average_sentiment

# Find category with the highest and lowest sentiment
highest_sentiment_category = max(category_sentiments, key=category_sentiments.get)
lowest_sentiment_category = min(category_sentiments, key=category_sentiments.get)

# Create a graph
plt.figure(figsize=(6, 12))
plt.barh(list(category_sentiments.keys()), list(category_sentiments.values()))
plt.xlabel('Sentiment')
plt.ylabel('Category')
plt.title('Average Sentiment by Category')

# Label the points
plt.text(category_sentiments[highest_sentiment_category], highest_sentiment_category,
         f'Highest: {highest_sentiment_category}', ha='left', va='center')
plt.text(category_sentiments[lowest_sentiment_category], lowest_sentiment_category,
         f'Lowest: {lowest_sentiment_category}', ha='left', va='center')

# Show the graph
plt.tight_layout()
plt.show()
