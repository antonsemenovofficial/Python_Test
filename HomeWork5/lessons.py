from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://repetitor-alexeeva.ru")
driver.save_screenshot('./test.png')

  
#driver.back()
#driver.forward()
#driver.refresh()









sleep(15)