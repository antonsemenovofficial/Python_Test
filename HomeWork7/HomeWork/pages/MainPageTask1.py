from selenium.webdriver.common.by import By

class MainPageTask1:

    def __init__(self, browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_seconds(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").click()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(term)


