from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def make_screenshoot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru")
    sleep(5)

    browser.save_screenshot('./ya_' + browser.name + '.png')
    browser.quit()


firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


make_screenshoot(chrome)
make_screenshoot(firefox)