from pages.customer_page import CustomerPage


def test_customer_module(driver):
    customer = CustomerPage(driver)

    print("➡️ Opening customer module")
    customer.open_customer_module()

    print("➡️ Clicking Details")
    customer.click_details()

    print("➡️ Clicking New")
    customer.click_new()

    print("➡️ Filling customer form")
    customer.fill_customer_form(
        last_name="Saif",
        first_name="Minus",
        company="IIFA",
        address="102 Pali hills",
        address2="Street style",
        city="New York",
        state="NY",
        zipcode="10046"
    )

    print("➡️ Clicking Save")
    customer.click_save()

    print("➡️ Tapping outside to dismiss keyboard")
    customer.tap_outside()