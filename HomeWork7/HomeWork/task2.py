from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPageTask2 import MainPageTask2
from pages.CalculatorPage import CalculatorPage

def test_calculator():
    browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    main_page = MainPageTask2(browser)
    main_page.get()
    main_page.set_seconds('45')

    calculator_page = CalculatorPage(browser)
    calculator_page.first_number()
    calculator_page.operator()
    calculator_page.second_number()
    calculator_page.ravno()

    calculator_page.result()