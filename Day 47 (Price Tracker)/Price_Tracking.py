import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Sony-SSCS5-3-Driver-Bookshelf-Speaker/dp/B00O8YLMVA/ref=sr_1_4?crid=3UM0S87WKOO5Y&keywords=speakers&qid=1694006581&sprefix=speake%2Caps%2C544&sr=8-4&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

print(f"The price is: '{price_as_float}'!")


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("goodmanjoe98@gmail.com", "nenjwxyfhqfwdsyv")
    server.sendmail(
        "lysychlop@gmail.com",
        ["lysychlop@gmail.com"],
        "Subject: Instant Pot Duo!\n\nI've finally found a speaker for less than $100! Check it out: https://www.amazon.com/Sony-SSCS5-3-Driver-Bookshelf-Speaker/dp/B00O8YLMVA/ref=sr_1_4?crid=3UM0S87WKOO5Y&keywords=speakers&qid=1694006581&sprefix=speake%2Caps%2C544&sr=8-4&th=1"
    )
print("successfully sent email")





    # with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        # connection.starttls()
        # result = connection.login(nes, YOUR_PASSWORD)
        # connection.sendmail(
            # from_addr=YOUR_EMAIL,
            # to_addrs=YOUR_EMAIL,
            # # msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        # )