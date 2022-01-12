import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Accept-Language": "en-au"
}
response = requests.get(url=URL, headers=headers)
content = response.text

# ------------------BS4----------------#

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
# print(len(listings)) # gives 41 / 42 results
listing_links_list = []
listing_price_list = []
listing_address_list = []
counter = 0

# delete all scripts
scripts = soup.find_all("script")
for script in scripts:
    script.decompose()
# populate listing_links_list & listing_price_list
# only goes through 9 listings, need to scroll (with selenium) to get others
for listing in listings:
    try:
        listing.contents[0]
    except IndexError:
        pass
    else:
        if listing.contents[0].get("id") == "nav-ad-container":
            pass
        else:
            if listing.contents[0].get("id") == "zpid_2066830464":
                pass
            else:
                counter += 1
                info = listing.contents[0].contents[0]
                # get link
                try:
                    info.findChild("a")['href']
                except TypeError:
                    pass
                else:
                    if "http" not in info.findChild("a")['href']:
                        link = f"https://www.zillow.com{info.findChild('a')['href']}"
                    else:
                        link = info.findChild("a")['href']
                    # get price
                    price = info.contents[2].contents[0].getText()
                    # add both to respecitve lists
                    address = info.contents[0].getText()
                    listing_links_list.append(link)
                    listing_price_list.append(price)
                    listing_address_list.append(address)

print(listing_links_list)
print(listing_price_list)
print(listing_address_list)

# ------------------SELENIUM----------------#
DRIVER_PATH = "/Users/maximus/Documents/dev_doc/chromedriver"
FORM_URL = "https://forms.gle/gEGuTzb3TwxHcWgS8"
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15')
CHROME_OPTIONS.add_argument('--accept-language=en-au')
CHROME_OPTIONS.add_argument('--accept-encoding=gzip, deflate')
CHROME_OPTIONS.add_argument('--connection=keep-alive')
CHROME_OPTIONS.add_argument('--cookie=_ga=GA1.2.1078659744.1641523811')
CHROME_OPTIONS.add_argument('--upgrade-insecure-request=1')
CHROME_OPTIONS.add_argument('--request-line=GET / HTTP/1.1')

S = Service(DRIVER_PATH)

driver = webdriver.Chrome(service=S, options=CHROME_OPTIONS)

driver.implicitly_wait(30)
wait = WebDriverWait(driver, 30)
driver.get(FORM_URL)



# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15