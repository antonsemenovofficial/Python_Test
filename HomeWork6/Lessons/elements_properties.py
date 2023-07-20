from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# driver.get("https://yandex.ru")

# txt = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Курс USD/RUB']").text
# tag = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Курс USD/RUB']").tag_name
# id = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Курс USD/RUB']").id
# href = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Курс USD/RUB']").get_attribute("href")
# ff = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Курс USD/RUB']").value_of_css_property("font-family")
# color = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Курс USD/RUB']").value_of_css_property("color")

# print(txt)
# print(tag)
# print(id)
# print(href)
# print(ff)
# print(color)

# driver.get("http://www.uitestingplayground.com/visibility")

# is_dispayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_dispayed)
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
# sleep(2)
# is_dispayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_dispayed)
# sleep(2)

# driver.get("https://demoqa.com/radio-button")

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)

# driver.get("https://the-internet.herokuapp.com/checkboxes")

# cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")

# is_selected = cb.is_selected()
# print(is_selected)

# cb.click()

# is_selected = cb.is_selected()
# print(is_selected)

driver.get("https://the-internet.herokuapp.com/checkboxes")

# div = driver.find_element(By.CSS_SELECTOR,"#page-footer")

# a = div.find_element(By.CSS_SELECTOR, "a")

# print(a.get_attribute("href"))

divs = driver.find_elements(By.CSS_SELECTOR, "div")

div = divs[6]
css_class = div.get_attribute("class")
print(css_class)