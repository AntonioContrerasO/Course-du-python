import datetime as dt
import math

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
appi_key_alpha = "Q0JTH77CNC8APNXT."
news_key = "71366185db324db89f4353ce473fac79"
account_sid = "AC106296c97ef6fdd940deb0aeec3dbd2c"
auth_token = "22a448add80422df33e8d23de45903aa"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": appi_key_alpha
}

year = dt.datetime.now().year
month = dt.datetime.now().month
yesterday = dt.datetime.now().day - 1
yesterday_of_yesterday = yesterday - 1

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()

close_yesterday = float(data["Time Series (Daily)"][f"2022-01-07"]["4. close"])
close_y_y = float(data["Time Series (Daily)"][f"2022-01-06"]["4. close"])

percentage = (close_yesterday - close_y_y) / close_y_y * 100
round_per = math.floor(percentage)
if abs(percentage) < 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    params_news = {
        "q": COMPANY_NAME,
        "apiKey": news_key
    }

    response_news = requests.get(url="https://newsapi.org/v2/everything", params=params_news)
    data = response_news.json()
    news_3 = data["articles"][:3]
    titles = [news_3[i]["title"] for i in range(len(news_3))]
    descriptions = [news_3[i]["description"] for i in range(len(news_3))]
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    for i in range(0, 3):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{round_per}%"
                 f"---{titles[i]}---\n {descriptions[i]}",
            from_='+19387777541',
            to='+526643676744'
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
