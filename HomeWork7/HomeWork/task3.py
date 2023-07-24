from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPageTask3 import MainPageTask3
from pages.CatalogPage import CatalogPage
from pages.CartPage import CartPage

def test_online_shop():
    browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    main_page = MainPageTask3(browser)

    main_page.get()
    main_page.login('standard_user')
    main_page.password('secret_sauce')
    main_page.button_login()

    catalog_page = CatalogPage(browser)

    catalog_page.add_to_cart()
    catalog_page.to_cart()
    
    cart_page = CartPage(browser)

    cart_page.checkout()
    cart_page.first_name('f')
    cart_page.last_name('f')
    cart_page.postal_code('f')
    cart_page.continues()
    totals = cart_page.total()


    assert totals == "Total: $58.29"
