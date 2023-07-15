from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

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