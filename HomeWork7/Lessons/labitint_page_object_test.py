from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage

cookie = {
    "name": "cookie_policy",
    "value": "1"
}

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('python')

    result_page = ResultPage(browser)
    result_page.table()
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get()
    as_is = cart_page.get_counter()

    assert as_is == to_be




