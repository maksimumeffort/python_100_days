import requests
# from datetime import date, timedelta
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "XQ3DHL6ZLDDELUFW"
news_api_key = "8d2dec04ef20460a85aada7fbb879a98"
max_num = 10

# today = date.today()
# yesterday = today - timedelta(days=1)
# day_before = str(yesterday - timedelta(days=1))


stock_params ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

news_params = {
    "apiKey": news_api_key,
    "qInTitle": COMPANY_NAME,
    "pageSize": max_num
}


## STEP 1: Use https://www.alphavantage.co/query
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]

yesterday_close = float(stock_list[0]["4. close"])
day_before_close = float(stock_list[1]["4. close"])

difference = yesterday_close - day_before_close
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / yesterday_close) * 100)

five_percent = abs(difference) > 0.05 * yesterday_close

# print(abs(yesterday_close - day_before_close))
#
# print(diff_percent)
# print(0.0128 * yesterday_close)
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

if five_percent:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_data = news_response.json()
    first_3 = news_data["articles"][:3]
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    #HINT 1: Think about using the Python Slice Operator


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.
    account_sid = 'AC759fe92fa01dad49f602eff2663d0549'
    auth_token = 'ac3926ba01a7da975390366979084391'
    client = Client(account_sid, auth_token)

    articles_list = [f"\nHeadline: {article['title']}. \nBrief: {article['description']}\n" for article in first_3]
    text = f"\n{STOCK}: {up_down}{diff_percent}%"
    for article in articles_list:
        text += article

    message = client.messages \
                    .create(
                         body=text,
                         from_='+14159157364',
                         to='+61459619924'
                     )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

