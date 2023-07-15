from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

input = "input"

input_in = driver.find_element(By.CSS_SELECTOR, input)
sleep(2)

input_in.send_keys('1000')
sleep(1)
input_in.clear()
sleep(1)
input_in.send_keys('999')
sleep(2)

driver.close()