from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)

driver.get("https://www.amazon.com/Apple-MWP22AM-A-cr-AirPods-Renewed/dp/B0828BJGD2/?_encoding=UTF8&pd_rd_w=gghzK&content-id=amzn1.sym.7f957896-9457-4ac3-8c2b-58f2b6be2857&pf_rd_p=7f957896-9457-4ac3-8c2b-58f2b6be2857&pf_rd_r=HSG9WQ0WWBVJ3K9AFH6R&pd_rd_wg=9qpou&pd_rd_r=93733208-cf1e-4ac8-8743-aa3c3270d521&ref_=pd_gw_exports_top_sellers_unrec&th=1")

item = driver.find_element(By.ID, "productTitle").text

price = driver.find_element(By.CSS_SELECTOR, "#corePrice_desktop > div > table > tbody > tr > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay > span:nth-child(2)").text

print(f"You want to buy '{item}'!\nAND the cost is only: £{price}!!")


