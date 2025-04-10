import os
import pytest
from drivers.driver_factory import create_driver
from datetime import datetime

# Required for attaching screenshots to HTML report
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

@pytest.fixture
def driver(request):
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(file_path)

            # Embed screenshot in the HTML report
            if hasattr(rep, "extra"):
                extra = rep.extra
            else:
                extra = []
            extra.append(pytest_html.extras.image(file_path))
            rep.extra = extra
