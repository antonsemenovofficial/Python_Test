from selenium.webdriver.common.by import By

class CatalogPage:

    def __init__(self, browser):
        self.driver = browser
    
    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    def to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()



