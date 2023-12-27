from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

ACCOUNT_EMAIL = "nesaar97@gmail.com"
ACCOUNT_PW= "Vitamins123!"

# OPTIONAL - Keeps the web browser open!

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)


# REJECT COOKIES OR pop-ups
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="Deny"]')
reject_button.click()

# Click sign in. 
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# ACTUALLY SIGN IN
time.sleep(5)
email_field = driver.find_element (by=By.ID, value = ACCOUNT_EMAIL)
email_field.send_keys (ACCOUNT_EMAIL)

password_field = driver.find_element (by=By.ID, value = ACCOUNT_PW)
password_field.send_keys(ACCOUNT_PW)
password_field.send_keys(Keys.Enter)

# IF There is a Captcha 

input("Press Enter when you have solved the Captcha")