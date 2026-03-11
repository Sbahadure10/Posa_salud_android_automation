import time
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from appium.webdriver.common.appiumby import AppiumBy


def test_logout(driver):

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

    login_screen = driver.find_elements(
        AppiumBy.XPATH, "//android.widget.EditText"
    )

    assert len(login_screen) > 0, "Logout failed: Login screen not visible"