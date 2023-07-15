from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")


button = "button.btn.class1.btn-primary.btn-test"

button_click_without_id = driver.find_element(By.CSS_SELECTOR, button)
sleep(2)

button_click_without_id.click()

driver.close()