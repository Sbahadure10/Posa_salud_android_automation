import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    # Connect to the Expo Go app (dev build runs inside Expo Go container)
    options.app_package = "host.exp.exponent"
    options.app_activity = "host.exp.exponent.experience.HomeActivity"
    options.no_reset = True
    options.dont_stop_app_on_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """Provide a LoginPage instance after waiting for the app to load."""
    time.sleep(3)
    return LoginPage(driver)