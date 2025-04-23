from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# articvle_title = soup.select_one(selector=".titleline a").getText() # Get the first articles title text
# article_link = soup.select_one(selector=".titleline a").get("href") # Gets the href attribute from first article
# article_upvotes = soup.select_one(selector=".score").getText() # Get total upvotes from first element

# Adding multiple entries to lists
articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article in articles:

    article_title = article.getText()
    article_texts.append(article_title)
    article_link = article.get("href")
    article_links.append(article_link)

upvotes = soup.select(selector=".score")
article_upvotes = []
for upvote in upvotes:
    article_upvotes.append(int(upvote.getText().split(" ")[0]))

highest_upvote =article_upvotes.index(max(article_upvotes))
print(article_texts[highest_upvote])
print(article_links[highest_upvote])
print(article_upvotes[highest_upvote])