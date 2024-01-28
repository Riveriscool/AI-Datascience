import requests
import pandas as pd
from datetime import datetime, timedelta
import random
from textblob import TextBlob

# Define the endpoint
url = 'https://newsapi.org/v2/everything?'

# Specify the query and number of returns
parameters = {
    'q': 'AMZN',  # query phrase
    'sortBy': 'popularity',  # articles from popular sources and publishers come first
    'pageSize': 100,  # maximum is 100 for developer version
    'apiKey': '50307a5da5ad4f5db9525c5ca1379260',  # your own API key
}

start_date = datetime(1998, 1, 1)
end_date = datetime.now()
current_date = start_date

headlines = []

while current_date <= end_date:
    formatted_date = current_date.strftime('%Y-%m-%d')
    parameters['from'] = formatted_date
    parameters['to'] = formatted_date

    # Make the request
    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()
        if data['totalResults'] > 0:
            for article in data['articles']:
                headline = article['title']
                headlines.append((formatted_date, headline))
        else:
            neutral_headline = generate_neutral_headline()
            headlines.append((formatted_date, neutral_headline))
    else:
        print(f"Error occurred for date {formatted_date}: {response.status_code}")

    current_date += timedelta(days=1)

# Create DataFrame from headlines
df = pd.DataFrame(headlines, columns=['Date', 'Headline'])

# Save DataFrame to Excel file
df.to_excel('news_headlines.xlsx', index=False)
