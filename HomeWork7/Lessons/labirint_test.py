from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_cart_counter():
    browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    ##перейти на сайт лабиринта
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

    ##найти книги по Питону
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("Python")
    browser.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
    ##переключиться на таблицу

    ##перейти на сайт лабиринта

    ##добавить все книги в коррзину и посчитать, сколько

    ##перейти в корзину

    ##поверить счетчик товаров

    sleep(5)


    browser.quit()