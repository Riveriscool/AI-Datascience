from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='cf4e76c3690d4f7eaa0e162699e9ea33')
"""
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='AMZN',
                                          sources='Wall-street-journal,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
print(top_headlines)"""