import time
from pages.login_page import LoginPage


def test_login(driver):
    """Test that valid credentials navigate from login screen to home screen."""
    time.sleep(3)  # Wait for app to fully load

    login = LoginPage(driver)
    login.login("chris@example.com", "Test@123")

    # Wait for navigation to complete
    time.sleep(10)

    # Verify we navigated away from the login screen
    page_source = driver.page_source
    assert "Login Here" not in page_source, (
        "Login failed: still on the login screen after entering valid credentials"
    )
