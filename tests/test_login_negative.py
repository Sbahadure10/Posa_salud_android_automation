import pytest


def test_empty_fields(login_page):

    login_page.click_login()

    validation = login_page.get_validation_message()

    assert "Invalid username or email address" in validation


def test_empty_userid(login_page):

    login_page.clear_fields()

    login_page.enter_password("Test@123")
    login_page.click_login()

    validation = login_page.get_validation_message()

    assert "Invalid username or email address" in validation


def test_empty_password(login_page):

    login_page.clear_fields()

    login_page.enter_email("chris@example.com")
    login_page.click_login()

    validation = login_page.get_validation_message()

    assert "Password" in validation or "Invalid username" in validation


def test_special_characters_userid(login_page):

    login_page.clear_fields()

    login_page.enter_email("@#$%")
    login_page.enter_password("Test@123")
    login_page.click_login()

    validation = login_page.get_validation_message()

    assert "Invalid username or email address" in validation


def test_invalid_password(login_page):

    login_page.clear_fields()

    login_page.enter_email("chris@example.com")
    login_page.enter_password("wrongpassword")
    login_page.click_login()

    error = login_page.get_error_popup()

    assert "Invalid credentials. Please check your email or password" in error

    login_page.close_error_popup()


def test_password_below_minimum(login_page):

    login_page.clear_fields()

    login_page.enter_email("chris@example.com")
    login_page.enter_password("123")
    login_page.click_login()

    error = login_page.get_error_popup()

    assert "Invalid credentials. Please check your email or password" in error

    login_page.close_error_popup()


def test_trim_spaces(login_page):

    login_page.clear_fields()

    login_page.enter_email(" chris@example.com ")
    login_page.enter_password(" Test@123 ")
    login_page.click_login()

    error = login_page.get_error_popup()

    assert "Invalid credentials. Please check your email or password" in error

    login_page.close_error_popup()


def test_invalid_userid(login_page):

    login_page.clear_fields()

    login_page.enter_email("chris222@example.com")
    login_page.enter_password("Test@123")
    login_page.click_login()

    error = login_page.get_error_popup()

    assert "Email is not registered. Please sign up." in error

    login_page.close_error_popup()


def test_both_credentials_invalid(login_page):

    login_page.clear_fields()

    login_page.enter_email("chris2222@example.com")
    login_page.enter_password("Test@123455677")
    login_page.click_login()

    error = login_page.get_error_popup()

    assert "Email is not registered. Please sign up." in error

    login_page.close_error_popup() 