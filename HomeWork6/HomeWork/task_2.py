from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

sleep(5)

input_in = driver.find_element(By.CSS_SELECTOR, "input").click()

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print('Кнопка до изменения ' + txt)

input_in = driver.find_element(By.CSS_SELECTOR, "input")

input_in.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print('Кнопка после изменения ' + txt)

sleep(5)