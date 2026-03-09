from pages.logout_page import LogoutPage

def test_logout(driver):

    logout = LogoutPage(driver)

    logout.open_menu()
    logout.sign_out_user()
    logout.confirm_logout_user()