from selenium.webdriver.common.by import By

class MainPageTask1:

    def __init__(self, browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def first_name(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(term)
    
    def last_name(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(term)

    def address(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(term)

    def email(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(term)
    
    def phone_number(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(term)

    def zip_code(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(term)

    def city(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(term)

    def country(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(term)
    
    def job_position(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(term)

    def company(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(term)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

    def get_red_zip_code(self):
        id_zip = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").text
        if id_zip == 'zip-code':
            div = self.driver.find_element(By.CSS_SELECTOR, "div.alert.py-2.alert-danger")
            div_red = div.get_attribute("class")
            return div_red.text
        print(id_zip)

