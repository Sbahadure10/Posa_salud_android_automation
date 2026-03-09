import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout(driver):
    """Test that a logged-in user can successfully log out."""
    time.sleep(3)

    # Login first
    login = LoginPage(driver)
    login.login("chris@example.com", "Test@123")
    time.sleep(8)

    # Click the close (cross) button if present
    try:
        close_button = driver.find_element(
            AppiumBy.XPATH,
            "//android.view.ViewGroup[.//android.widget.ImageView]"
        )
        close_button.click()
        print("Closed error popup")
        time.sleep(2)
    except:
        print("Close button not present")

    # Continue with logout
    logout = LogoutPage(driver)
    logout.open_menu()
    logout.sign_out_user()
    logout.confirm_logout_user()