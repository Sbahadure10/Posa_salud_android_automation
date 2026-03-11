import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_menu(self):
        menu = self.driver.find_element(
            AppiumBy.XPATH, "(//com.horcrux.svg.J)[1]"
        )
        menu.click()
        time.sleep(5)

    def sign_out_user(self):
        sign_out = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Sign')]")
            )
        )
        sign_out.click()

    def confirm_logout_user(self):

        # wait for the confirmation dialog
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Logout")
            )
        )

        logout_btn.click()