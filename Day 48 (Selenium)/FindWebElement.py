from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Can interact with Chrome, Safari and Firefox
    # Keep it open with OPTIONS 
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
# price_cents = driver.find_element(By.CLASS_NAME, value= 'a-price-fraction').text

# print(f"The price is: ${price_dollar}.{price_cents}!")

driver.get("https://www.python.org")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
print(search_bar.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)





#close vs quit
# close closes a single tab
# quit will exit the ENTIRE browser

#driver.quit()