from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://ya.ru")
driver.get("https://vk.com")

for x in range(1.10):   
    driver.back()
    driver.forward()









sleep(15)