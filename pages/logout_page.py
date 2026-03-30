from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_menu(self):

        # ✅ Wait for menu icon (NOT 3 dots)
        menu = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "(//com.horcrux.svg.J)[1]")
            )
     )
        menu.click()

        # ✅ Click 3 dots again (fresh element)
        menu = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "")
            )
        )
        menu.click()

    def sign_out_user(self):
        sign_out = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Sign')]")
            )
        )
        sign_out.click()

    def confirm_logout_user(self):
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Logout")
            )
        )
        logout_btn.click()