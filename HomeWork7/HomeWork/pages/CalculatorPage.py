from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPageTask1 import MainPageTask1


class CalculatorPage:

    def __init__(self, browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def first_number(self):
        key = self.driver.find_element(By.CSS_SELECTOR, "div.keys > span:nth-child(1)").click()
   
    def operator(self):
        key = self.driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()

    def second_number(self):
        key = self.driver.find_element(By.CSS_SELECTOR, "div.keys > span:nth-child(2)").click()
    
    def ravno(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()

    def result(self):
        results = '15'
        WebDriverWait(self.driver, 70).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"),results)
        )
    
    def result_1(self):
        results = '15'
        WebDriverWait(self.driver, 70).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"),results)
        )
        result_1 = self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result_1
