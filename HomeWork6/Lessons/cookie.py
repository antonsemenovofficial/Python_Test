from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
cookie = {
    'name' : 'cookie_policy',
    'value' : '1'
}


driver.get("https://labirint.ru")

driver.add_cookie(cookie)
driver.refresh()

driver.delete_all_cookies()
driver.refresh()

sleep(10)
driver.quit()

