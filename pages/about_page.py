from selenium.webdriver.common.by import By

class AboutPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_header(self):
        header = self.driver.find_element(By.TAG_NAME, "h1")
        return header.text

    def get_subheader(self):
        subheader = self.driver.find_element(By.TAG_NAME, "h2")
        return subheader.text