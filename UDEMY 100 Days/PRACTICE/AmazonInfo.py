from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome=chrome)
driver.get()