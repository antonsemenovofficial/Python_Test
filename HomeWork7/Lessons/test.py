from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(7)
    

driver.find_element(By.CSS_SELECTOR, "#user-name").click()
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#user-name").click()
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()  
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

driver.find_element(By.CSS_SELECTOR, "#checkout").click()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("F")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("F")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("FF")
driver.find_element(By.CSS_SELECTOR, "#continue").click()

txt = driver.find_element(By.CSS_SELECTOR, "div.summary_info_label.summary_total_label").text

print(txt)