# STOCK APIs
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "1Y7ONFWIAHRKSAKF"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
#PUT KEY HERE
stock_data = response.json()["Time Series (Daily)"]
#print(stock_data)

#Large Dictionary --> Easier to turn into a LIST
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_data)
print(yesterday_closing_price)
#yesterday_closing_price = b

#print(stock_data_list)
