from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc = response.text

soup = BeautifulSoup(yc, "html.parser")
# article_text = soup.select_one(selector="td.title a").get_text()
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

# article_upvote = soup.select_one(selector="td.subtext span").getText()
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_num = max(article_upvotes)
max_index = article_upvotes.index(largest_num)
# print(article_upvotes)
print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])







#
# with open("website.html") as doc:
#     contents = doc.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # soup = python object
# # print(soup.prettify())
# # print(soup.li)
#
# all_anchors = soup.find_all(name="a")
# # print(all_anchors)
#
# for tag in all_anchors:
#     pass
#     #print(tag.get("href"))
#     #print(tag.getText())
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(class_="heading")
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")  # gives first matching item in list (a tag that's inside p tag)
# name_id = soup.select_one(selector="#name")
# heading_class = soup.select(selector=".heading")  # gives list of all items with specified selector
# print(name_id)
# print(company_url)
# print(heading_class)
