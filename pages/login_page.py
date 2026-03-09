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

    def clear_fields(self):
        """Clear email and password fields."""
        fields = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.EditText")
        for field in fields:
            field.click()
            field.clear()
            # React Native state isn't cleared by field.clear(), so send backspaces via ADB
            self.driver.execute_script("mobile: shell", {"command": "input", "args": ["keyevent", "123"]}) # Move to End
            for _ in range(50):
                self.driver.execute_script("mobile: shell", {"command": "input", "args": ["keyevent", "67"]}) # Backspace
            time.sleep(0.5)

    def get_validation_message(self):
        """Get validation message shown inline on the login screen."""
        wait = WebDriverWait(self.driver, 10)
        msg = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//*[contains(@text,'Invalid username')]")
            )
        )
        return msg.text


    def get_error_popup(self):
        """Get popup error message for invalid credentials."""
        wait = WebDriverWait(self.driver, 10)
        msg = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//*[contains(@text,'Invalid credentials')]")
            )
        )
        return msg.text


    def close_error_popup(self):
        """Tap screen to dismiss popup error message."""
        self.driver.execute_script("mobile: clickGesture", {
            "x": 500,
            "y": 1500,
        })