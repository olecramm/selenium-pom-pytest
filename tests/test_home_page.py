import time
from pages.home_page import HomePage

def test_home_page_title(driver):
    title_selenium = "Selenium"

    # Create an instance of the HomePage class
    home_page = HomePage(driver)
    url = "https://www.selenium.dev/"

    # Navigate to the home page
    driver.get(url)

    # Get the title of the page
    title = home_page.get_title()

    time.sleep(5)  # Wait for the page to load

    # Assert that the title is correct
    assert title_selenium == title, f"Expected title: {title_selenium}, but got: {title}"