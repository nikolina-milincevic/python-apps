import requests

# this is an app for getting email with news

# these data are from the teacher of the course
# I would need to go to newapi.org, make an account
# and copy my own key

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?" \
    "q=tesla&sortBy=publishedAt&"\
    "apiKey=890603a55bfa47048e4490069ebee18c"

request = requests.get(url)
content = request.text
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
