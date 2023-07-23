from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    sleep(4)

    ##переключиться на таблицу
    browser.find_element(By.CSS_SELECTOR,"a[title='таблицей']").click()

    WebDriverWait(browser, 20).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )

    ##добавить все книги в коррзину и посчитать, сколько
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    ##перейти в корзину
    browser.get("https://www.labirint.ru/cart/")
    ##поверить счетчик товаров
    txt = browser.find_element(By.CSS_SELECTOR,"a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, "b").text

    assert counter == int(txt)


    browser.quit()