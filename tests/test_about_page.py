import time
from pages.home_page import HomePage
from pages.navbar import NavBar

def test_about_page_title(driver):
    """
    Test the title of the About page.
    This test verifies that the title of the About page is correct.
    """
    # Expected title
    title_selenium = "About Selenium | Selenium"

    # Create an instance of the HomePage class
    home_page = HomePage(driver)

    # Navigate to the home page
    home_page.navigate_to_home_page()

    # Create an instance of the NavBar class
    navbar = NavBar(driver)

    # Click on About link in the navbar
    navbar.click_navbar()

    # Click on About Selenium link in the dropdown
    about_page = navbar.click_about_dropdown_item()

    # Verify the title of the About page
    assert title_selenium == about_page.get_title(), f"Expected title: {title_selenium}, but got: {driver.title}"
    time.sleep(2)  # Optional: Pause for 2 seconds to observe the result

