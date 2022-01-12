import requests
from bs4 import BeautifulSoup

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Accept-Language": "en-au"
}

response = requests.get(url=URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")
# tag_list = soup.find_all('a', 'list-card-link')
# links_list = []
# for tag in tag_list:
#     link = tag.get("href")
#     if "http" not in link:
#         links_list.append(f"https://www.zillow.com{link}")
#     else:
#         links_list.append(link)
price_list = soup.find('ul', {"class": "photo-cards"})
listings = price_list.findChildren(recursive=False)
listing_links_list = []
listing_price_list = []
counter = 0
# delete all scripts
scripts = soup.find_all("script")
for script in scripts:
    script.decompose()

for listing in listings[:1]:
    print(listing.contents[0])
#     counter +=1
#     try:
#         article = listing.contents[1]
#     except:
#         pass
#     else:
#         card_info = article.contents[0]
#         # get link
#         link = card_info.contents[0].get("href")
#         listing_links_list.append(link)
#         # get price
#         price = card_info.contents[2].contents[0].getText()
#     print(f"{counter} down")






