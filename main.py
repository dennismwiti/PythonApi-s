import requests

api_key = "73d67d6cfe6e4c3aa0094b9555a343ce"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-12&sortBy=publishedAt&apiKey=" \
      "73d67d6cfe6e4c3aa0094b9555a343ce"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description.
for article in content['articles']:
    print(article['title'])
    print(article['description'])
