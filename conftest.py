import os
import pytest
from datetime import datetime
from drivers.driver_factory import create_driver

@pytest.fixture
def driver(request):
    driver = create_driver()
    yield driver
    driver.quit()

# Required for attaching screenshots to HTML report
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

    #Create a directory for the reports if it doesn't exist
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Timestamped report file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = os.path.join(reports_dir, f"report_{timestamp}.html")

    # Set report path and options
    config.option.htmlpath = report_file
    config.option.self_contained_html = True
    config.option.css = ["custom.css"]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

            # Correct path to save the screenshot
            file_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(file_path)

            # Relative path for HTML report (from report HTML's perspective)
            relative_path = os.path.join("screenshots", file_name).replace("\\", "/")

            # Embed screenshot in the HTML report
            if hasattr(rep, "extra"):
                extra = rep.extra
            else:
                extra = []
            extra.append(pytest_html.extras.image(relative_path))
            rep.extra = extra
