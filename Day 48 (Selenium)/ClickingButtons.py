from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Nesaar")
time.sleep(1)

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Uppal")
time.sleep(1)

email = driver.find_element(By.NAME, "email")
email.send_keys("nesaar7@gmail.com")
time.sleep(1)

submit = driver.find_element(By.CSS_SELECTOR, "form.form-signin button")
submit.click()