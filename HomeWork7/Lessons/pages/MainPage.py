class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.labirint.ru")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }
        self.driver.add_cookie(cookie)