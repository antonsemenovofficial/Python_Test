from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser):
        self.driver = browser

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    
    def first_name(self,trem):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(trem)

    def last_name(self,trem):
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(trem)

    def postal_code(self,trem):
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(trem)
    
    def continues(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def total(self):
        self.driver.find_element(By.CSS_SELECTOR, "div.summary_info_label.summary_total_label").text
        self.driver.quit()

    



