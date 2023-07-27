from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPageTask1 import MainPageTask1

def test_red_field():
    browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    main_page = MainPageTask1(browser)
    main_page.get()
    main_page.first_name('Иван')
    main_page.last_name('Петров')
    main_page.address('Ленина, 55-3')
    main_page.email('test@skypro.com')
    main_page.phone_number('+7985899998787')
    main_page.zip_code('')
    main_page.city('Москва')
    main_page.country('Россия')
    main_page.job_position('QA')
    main_page.company('SkyPro')
    main_page.submit()

    zip = main_page.get_red_zip_code()
    fn = main_page.check_first_name()
    ln = main_page.check_last_name()
    address = main_page.check_address()
    email = main_page.check_email()
    phone = main_page.check_phone()
    city = main_page.check_city()
    country = main_page.check_country()
    job = main_page.check_job()
    company = main_page.check_company()





    
    assert fn == 'alert py-2 alert-success'
    assert ln == 'alert py-2 alert-success'
    assert address == 'alert py-2 alert-success'
    assert email == 'alert py-2 alert-success'
    assert phone == 'alert py-2 alert-success'
    assert city == 'alert py-2 alert-success'
    assert country == 'alert py-2 alert-success'
    assert job == 'alert py-2 alert-success'
    assert company == 'alert py-2 alert-success'
    assert zip == 'alert py-2 alert-danger'
