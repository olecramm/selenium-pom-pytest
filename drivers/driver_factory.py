from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():

    options = Options()
    #options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--start-maximized")  # Start maximized
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")  

    print("[DEBUG] Headless mode is disabled!")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Set implicit wait time
    driver.implicitly_wait(10)  # Wait for elements to load
    return driver
