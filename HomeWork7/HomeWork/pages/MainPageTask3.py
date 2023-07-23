from selenium.webdriver.common.by import By

class MainPageTask3:

    def __init__(self, browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(7)
    
    def login(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").click()
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(term)
    
    def password(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").click()
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(term)
    
    def button_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()