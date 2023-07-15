from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

modal = 'div.modal-footer'

close_modal = driver.find_element(By.CSS_SELECTOR, modal)
sleep(2)

close_modal.click()

sleep(2)