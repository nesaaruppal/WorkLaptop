from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cursor = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[1]/div").text
cursor_str = cursor.strip("Cursor - ")
cursor_number = int(cursor)

grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma").text
grandma_str = grandma.strip("Grandma - ")
grandma_int = int(grandma_str)

factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory").text
factory_str = factory.strip("Factory - ")
factory_int = int(factory_str)

mine = driver.find_element(By.CSS_SELECTOR, "#buyMine").text
miner = mine.strip("Mine - ")
miner_int = int(miner)

shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment").text
shipments = shipment.strip("Shipment - ")
shipment_int = int(shipments)

alchemy_lab = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy lab").text
alchemy_button = alchemy_lab.strip("Alchemy - ")
alchemy_int = int(alchemy_button)

portal = driver.find_element(By.CSS_SELECTOR, "#buyPortal").text
portal_button = portal.strip("Portal - ")
portal_int = int(portal_button)

time_machine = driver.find_element(By.CSS_SELECTOR, "#buyTime machine").text
time_machine_button = time_machine.strip("Time machine - ")
time_machine_int = int(time_machine_button)


right_pane = [cursor_number, grandma_int, factory_int, miner_int, shipment_int, alchemy_int, portal_int, time_machine_int]

print(cursor_number)




submit = driver.find_element(By.ID, "cookie")
submit.click()
time.sleep(0.0000001)

print(right_pane)





