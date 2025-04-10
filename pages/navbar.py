from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.about_page import AboutPage

class NavBar(BasePage):

    # Locators
    LOCATOR_NAVBAR = (By.ID, "navbarDropdown")
    LOCATOR_ABOUT_DROPDOWN_ITEM = (By.XPATH, "//a[@class='dropdown-item'][normalize-space()='About Selenium']")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def click_navbar(self):
        self.click(locator=self.LOCATOR_NAVBAR)

    def click_about_dropdown_item(self):
        self.click_list_element(locator=self.LOCATOR_ABOUT_DROPDOWN_ITEM)
        return AboutPage(driver=self.driver)

        