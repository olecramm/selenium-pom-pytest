import time
from pages.home_page import HomePage

def test_home_page_title(driver):
    """
    Test the title of the home page.
    This test verifies that the title of the home page is correct.
    """
    # Expected title
    title_selenium = "Selenium"

    # Create an instance of the HomePage class
    home_page = HomePage(driver)

    # Navigate to the home page
    home_page.navigate_to_home_page()

    # Get the title of the page
    title = home_page.get_title()

    time.sleep(5)  # Wait for the page to load

    # Assert that the title is correct
    assert title_selenium == title, f"Expected title: {title_selenium}, but got: {title}"