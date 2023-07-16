from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 40)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#text"), "Done")
)

imgs = driver.find_elements(By.CSS_SELECTOR, "img")

img = imgs[3]
src = img.get_attribute("src")
print(src)