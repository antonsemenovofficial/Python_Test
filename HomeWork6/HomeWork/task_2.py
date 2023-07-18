from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

input_in = driver.find_element(By.CSS_SELECTOR, "input").click()

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print('Кнопка до изменения ' + txt)

input_in = driver.find_element(By.CSS_SELECTOR, "input")

input_in.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print('Кнопка после изменения ' + txt)

waiter = WebDriverWait(driver, 15, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#updatingButton"), "SkyPro"))

driver.quit()