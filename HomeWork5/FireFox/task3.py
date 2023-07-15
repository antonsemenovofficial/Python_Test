from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

button = "button"

button_click = driver.find_element(By.CSS_SELECTOR, button)
sleep(2)

button_click.click()
sleep(1)
button_click.click()
sleep(1)
button_click.click()
sleep(1)
button_click.click()
sleep(1)
button_click.click()
sleep(1)

delete_b = 'button.added-manually'
delete = driver.find_elements(By.CSS_SELECTOR, delete_b)

driver.close()

print(len(delete))