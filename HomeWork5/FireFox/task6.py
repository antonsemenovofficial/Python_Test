from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

modal = 'div.modal-footer'

close_modal = driver.find_element(By.CSS_SELECTOR, modal)
sleep(2)

close_modal.click()

sleep(2)

driver.close()