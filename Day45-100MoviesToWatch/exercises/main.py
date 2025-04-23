from bs4 import BeautifulSoup

with open("./Day45-100MoviesToWatch/exercises/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)

# Get all anchor tags
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText()) # Get text inside a tag
#     print(tag.get("href")) # Get the href attribute

# Finding by attribute name
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)

# Using CSS selectors to get specific anchor tag

# company_url = soup.select_one(selector="p a") # looks for an a tag within a p tag
# print(company_url)

headings = soup.select(selector=".heading") # Gets list of items with the class heading
print(headings)