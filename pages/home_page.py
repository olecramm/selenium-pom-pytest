from selenium.webdriver.common.by import By

class HomePage:

    URL= "https://www.selenium.dev/"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_home_page(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title
        