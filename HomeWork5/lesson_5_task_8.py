from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")


username = "#username"
password = "#password"
login_bt = "button.radius"

login_bt = driver.find_element(By.CSS_SELECTOR, login_bt)
username_set = driver.find_element(By.CSS_SELECTOR, username)
password_set = driver.find_element(By.CSS_SELECTOR, password)
username_set.click()
username_set.send_keys('tomsmith')
password_set.click()
password_set.send_keys('SuperSecretPassword!')
login_bt.click()


sleep(2)
