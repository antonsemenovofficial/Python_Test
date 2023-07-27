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
        id_zip = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property('class')
    
    def check_first_name(self):
        id_fn = self.driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property('color')

    def check_last_name(self):
        id_ln = self.driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property('class')
    
    def check_address(self):
        id_address = self.driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property('class')
    
    def check_phone(self):
        id_phone = self.driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property('class')
    
    def check_email(self):
        id_email = self.driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property('class')
    
    def check_city(self):
        id_city = self.driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property('class')
    
    def check_country(self):
        id_country = self.driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property('class')
    
    def check_job(self):
        id_job = self.driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property('class')
    
    def check_company(self):
        self.driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property('class')