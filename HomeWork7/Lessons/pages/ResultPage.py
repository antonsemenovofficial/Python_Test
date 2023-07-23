from typing import Self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:

    def __init__(self,browser):
        self.driver = browser
    
    def table():
        self.driver.find_element(By.CSS_SELECTOR,"a[title='таблицей']").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
        )

    def add_books():
        buy_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

        return counter