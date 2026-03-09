import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object for the login screen of the Posa Salud app.

    Uses ADB shell input for text entry, which is required for React Native
    apps where standard send_keys() doesn't trigger onChangeText events.
    Requires Appium started with: appium --allow-insecure='*:adb_shell'
    """

    def __init__(self, driver):
        self.driver = driver

    def _type_with_adb(self, text):
        """Type text using ADB shell input — simulates real OS-level keystrokes
        that trigger React Native's onChangeText reliably."""
        escaped = text.replace("\\", "\\\\")
        escaped = escaped.replace(" ", "%s")
        escaped = escaped.replace("&", "\\&")
        escaped = escaped.replace("<", "\\<")
        escaped = escaped.replace(">", "\\>")
        escaped = escaped.replace("(", "\\(")
        escaped = escaped.replace(")", "\\)")
        escaped = escaped.replace("|", "\\|")
        escaped = escaped.replace(";", "\\;")
        escaped = escaped.replace("'", "\\'")
        escaped = escaped.replace('"', '\\"')
        self.driver.execute_script("mobile: shell", {
            "command": "input",
            "args": ["text", escaped],
        })

    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 20)
        email_field = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.EditText[1]")
            )
        )
        email_field.click()
        time.sleep(0.5)
        self._type_with_adb(email)
        time.sleep(0.5)

    def enter_password(self, password):
        password_field = self.driver.find_element(
            AppiumBy.XPATH, "//android.widget.EditText[2]"
        )
        password_field.click()
        time.sleep(0.5)
        self._type_with_adb(password)
        time.sleep(0.5)

    def click_login(self):
        # Tap Login button using coordinates (center of bounds [65,1113][1015,1224])
        # Coordinate-based tap is more reliable for React Native TouchableOpacity
        self.driver.execute_script("mobile: clickGesture", {
            "x": 540,
            "y": 1168,
        })

    def login(self, email, password):
        """Convenience method to perform the full login flow."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
