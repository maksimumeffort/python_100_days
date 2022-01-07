import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
import smtplib

email = "throwawaytestemail2@gmail.com"
password = "5Tlny6lL45+tj)Nt"
receiver = "alexmaksimets@gmail.com"

URL = "https://www.amazon.com.au/SanDisk-128GB-microSDXC-Memory-Adapter/dp/B08GYKNCCP/ref=zg-bs_computers_2/356-7704280-8228115?pd_rd_w=7mPiU&pf_rd_p=cf40b4ab-6758-4067-925a-fd988196e92c&pf_rd_r=GNNYT7ARG5TZ005HRVTD&pd_rd_r=80dabc49-22bb-4050-82fd-523c0c1a90f5&pd_rd_wg=kwsj4&pd_rd_i=B08GYKNCCP&th=1"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Accept-Language": "en-au"
}

response = requests.get(url=URL, headers=HEADER)

soup = BeautifulSoup(response.text, "lxml")

price_whole = soup.find(name="span", class_="a-price-whole").get_text()
price_fraction = soup.find(name="span", class_="a-price-fraction").get_text()
total_price = float(f"{price_whole}{price_fraction}")

product_full_name = soup.find(name="span", id="productTitle").get_text()
product_title = product_full_name.split(" - ")[0]

print(total_price)

if total_price < 25:
    print("True")
    text = f"{product_title} is now {total_price}\n Buy @: {URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # makes the connection secure
        connection.login(user=email, password=password)  # logging in
        connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"Subject:Amazon Price Alert!\n\n{text}")
        print("completed")





