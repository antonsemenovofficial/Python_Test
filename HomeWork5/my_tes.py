from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://repetitor-alexeeva.ru/")
sign_in_button = '#sign'
name = '#stm-lms-register > form > div:nth-child(1) > div:nth-child(1) > div > input'
e_mail = '[placeholder="Введите свой e-mail"]'
password = '#stm-lms-register > form > div:nth-child(2) > div:nth-child(1) > div > input'
repeat_password = '[placeholder="Подтвердите пароль"]'
submit = 'button.btn.btn-default'

cabinet = driver.find_element(By.CSS_SELECTOR, sign_in_button).click()
name_1 = driver.find_element(By.CSS_SELECTOR, name)
email = driver.find_element(By.CSS_SELECTOR, e_mail)
password_1 = driver.find_element(By.CSS_SELECTOR, password)
repeat_password_1 = driver.find_element(By.CSS_SELECTOR, repeat_password)
sign = driver.find_element(By.CSS_SELECTOR, submit)

name_1.send_keys('Antonio')
email.send_keys('test@test.ru')
password_1.send_keys('@@Vjkjxysq1111')
repeat_password_1.send_keys('@@Vjkjxysq1111')

sign.click()

sleep(12)


