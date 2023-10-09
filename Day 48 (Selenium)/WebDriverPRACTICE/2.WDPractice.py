from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)

driver.get("https://www.amazon.com/")

search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("iPhone 13 Mini")
time.sleep(1)

submit = driver.find_element(By.ID, "nav-search-submit-button")
submit.click()
time.sleep(1)

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
iphone_price = int(price)

print(f"The iPhone costs £{iphone_price}!!")