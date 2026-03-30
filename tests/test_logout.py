from appium import webdriver
from appium.options.android import UiAutomator2Options
import unittest
import time
import pytest

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.skip(reason="Skipping logout test")
class TestLogout(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "Android Emulator"
        options.app_package = "com.yourapp.package"
        options.app_activity = "com.yourapp.MainActivity"

        self.driver = webdriver.Remote("http://localhost:4723", options=options)
        self.driver.implicitly_wait(10)

    def test_logout(self):

        driver = self.driver

        # ✅ Check if already logged out
        login_fields = driver.find_elements(
            AppiumBy.XPATH, "//android.widget.EditText"
        )

        if login_fields:
            login = LoginPage(driver)
            login.login("chris@example.com", "Test@123")

        logout = LogoutPage(driver)

        logout.open_menu()
        logout.sign_out_user()
        logout.confirm_logout_user()

        time.sleep(3)

        # ✅ Verify login screen appears
        login_screen = driver.find_elements(
            AppiumBy.XPATH, "//android.widget.EditText"
        )

        self.assertTrue(len(login_screen) > 0, "Logout failed")

    def tearDown(self):
        self.driver.quit()