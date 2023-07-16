from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/progressbar")

driver.find_element(By.CSS_SELECTOR,"#startButton").click()

waiter = WebDriverWait(driver, 40)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#progressBar"), "75%")
)


driver.find_element(By.CSS_SELECTOR,"#stopButton").click()


print( driver.find_element(By.CSS_SELECTOR,"#result").text ) 