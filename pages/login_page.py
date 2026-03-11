import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.EditText[1]")
            )
        )
        email_field.click()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.EditText[2]")
            )
        )
        password_field.click()
        password_field.send_keys(password)

    def tap_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//*[@text='Login']")
            )
        )
        login_button.click()

    # 👇 ADD THIS METHOD HERE
    def wait_for_home_screen(self):
        WebDriverWait(self.driver, 40).until(
            EC.invisibility_of_element_located(
                (AppiumBy.XPATH, "//*[contains(@text,'Login')]")
            )
        )
            
        

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.tap_login()

        # 👇 CALL THE WAIT METHOD
        self.wait_for_home_screen()