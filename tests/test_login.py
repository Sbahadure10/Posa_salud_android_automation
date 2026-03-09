from pages.login_page import LoginPage
<<<<<<< Updated upstream
=======
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
>>>>>>> Stashed changes


def test_login(driver):
    """Test that valid credentials log the user into the app."""

    login = LoginPage(driver)

    # perform login
    login.login("chris@example.com", "Test@123")

    print("Login attempted, waiting for home screen...")

    # wait for something on the home screen
    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, "//*[contains(@text,'Home')]")
        )
    )
<<<<<<< Updated upstream
=======

    print("Login successful.")
>>>>>>> Stashed changes
