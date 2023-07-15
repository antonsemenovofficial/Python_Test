from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://labirint.ru")

search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

books = driver.find_elements(By.CSS_SELECTOR, "div.product")

print(len(books))


for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'span.product-title').text
    author = ''
    price = book.find_element(By.CSS_SELECTOR, 'span.price-val').text

    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-author').text
    except:
        author = "Автор не указан"
    print(author + "\t" + title + "\t" + price)


sleep(5)