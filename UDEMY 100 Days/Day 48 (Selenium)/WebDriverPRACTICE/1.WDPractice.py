from selenium import webdriver

from selenium.webdriver.common.by import By
import smtplib
import time


chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)

driver.get("https://www.amazon.com")

# ratings = driver.find_element(By.ID, "acrCustomerReviewText")

# print(ratings.text)

search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("iPod")
time.sleep(0.5)

submit = driver.find_element(By.ID, "nav-search-submit-button")
submit.click()
time.sleep(0.5)

cost_ipod = driver.find_element(By.CLASS_NAME, "a-price-whole")
cost1 = (cost_ipod.text)
cost = int(cost1)


if cost > 100:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("goodmanjoe98@gmail.com", "nenjwxyfhqfwdsyv")
        server.sendmail(
        "goodmanjoe98@gmail.com",
        ["goodmanjoe98@gmail.com"],
        "Subject: iPod!!!!\n\nYou can afford an iPod! BUY IT!"
    )
    print("successfully sent email")
    print(f"£{cost}")
else:
    print("Too Expensive")
    print(f"£{cost}")