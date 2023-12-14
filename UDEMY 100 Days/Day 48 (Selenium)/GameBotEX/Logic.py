from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# game_on = True
# while game_on:
#     submit = driver.find_element(By.ID, "cookie")
#     submit.click()
#     time.sleep(0.000000000000000000000001)

cursor = driver.find_element(By.ID, "buyCursor").text
cursor_cost = driver.find_element(By.CSS_SELECTOR, "#buyCursor > b").text
cursor_button = int(cursor_cost.strip("Cursor - "))


grandma = driver.find_element(By.ID, "buyGrandma").text
factory = driver.find_element(By.ID, "buyFactory").text
mine = driver.find_element(By.ID, "buyMine").text
shipment = driver.find_element(By.ID, "buyShipment").text
alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab").text
portal = driver.find_element(By.ID, "buyPortal").text
time_machine = driver.find_element(By.ID, "buyTime machine").text



print(cursor_button)

list = [cursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine]


    cursor = driver.find_element(By.ID, "buyCursor").text
    grandma = driver.find_element(By.ID, "buyGrandma").text
    factory = driver.find_element(By.ID, "buyFactory").text
    mine = driver.find_element(By.ID, "buyMine").text
    shipment = driver.find_element(By.ID, "buyShipment").text
    alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab").text
    portal = driver.find_element(By.ID, "buyPortal").text
    time_machine = driver.find_element(By.ID, "buyTime machine").text

cursor = driver.find_element(By.ID, "buyCursor").text
cursor_cost = driver.find_element(By.CSS_SELECTOR, "#buyCursor > b").text


grandma = driver.find_element(By.ID, "buyGrandma").text
factory = driver.find_element(By.ID, "buyFactory").text
mine = driver.find_element(By.ID, "buyMine").text
shipment = driver.find_element(By.ID, "buyShipment").text
alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab").text
portal = driver.find_element(By.ID, "buyPortal").text
time_machine = driver.find_element(By.ID, "buyTime machine").text