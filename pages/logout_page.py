from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    hamburger_menu = (
        AppiumBy.XPATH,
        "//com.horcrux.svg.SvgView/ancestor::android.view.ViewGroup[1]"
    )

    sign_out = (
        AppiumBy.ACCESSIBILITY_ID,
        "Sign Out"
    )

    confirm_logout = (
        AppiumBy.ACCESSIBILITY_ID,
        "Logout"
    )

    def open_menu(self):
        menu = self.wait.until(
            EC.element_to_be_clickable(self.hamburger_menu)
        )
        menu.click()

    def sign_out_user(self):
        signout = self.wait.until(
            EC.element_to_be_clickable(self.sign_out)
        )
        signout.click()

    def confirm_logout_user(self):
        confirm = self.wait.until(
            EC.element_to_be_clickable(self.confirm_logout)
        )
        confirm.click()