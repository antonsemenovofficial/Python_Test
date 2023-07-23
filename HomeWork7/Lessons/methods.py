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

browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

def open_labirint():
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR,"button[type=submit]").click()

def table():
    browser.find_element(By.CSS_SELECTOR,"a[title='таблицей']").click()
    WebDriverWait(browser, 20).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )
def add_books():
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter

def open_cart():
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    txt =  browser.find_element(By.CSS_SELECTOR,"a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, "b").text
    return int(txt)


def test_cart_counter():
    open_labirint()
    search('python')
    table()

    added = add_books()
    open_cart()
    cart_counter = get_cart_counter()

    assert added == cart_counter

    browser.quit()