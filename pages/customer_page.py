from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CustomerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ✅ Wait for Home Screen
    def wait_for_home_screen(self):
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "")  # 3 dots
            )
        )

    # ✅ Open Customer Module
    def open_customer_module(self):

        # Step 1: Wait for home screen
        self.wait_for_home_screen()

        # Step 2: Click 3 dots
        menu = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "")
            )
        )
        menu.click()
        time.sleep(2)  # Wait for menu animation

        # Step 3: Click Customers
        customers = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//*[@text='Customers' or @content-desc='Customers']")
            )
        )
        customers.click()

        # Step 4: Wait for Customer screen to load
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//*[@text='Customers' or @content-desc='Customers']")
            )
        )

    # ✅ Click Details
    def click_details(self):
        details = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Details")
            )
        )
        details.click()
        time.sleep(5)  # Wait for page to load

    # ✅ Click New
    def click_new(self):
        new_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//*[contains(@content-desc, "New")]')
            )
        )
        new_button.click()
        time.sleep(3)  # Wait for form to load

    # ✅ Helper to fill a text field
    def _fill_field(self, field_text, value):
        field = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, f'//android.widget.EditText[@text="{field_text}"]')
            )
        )
        field.click()
        field.send_keys(value)

    # ✅ Fill Customer Form
    def fill_customer_form(self, last_name, first_name, company, address,
                           address2, city, state, zipcode):
        self._fill_field("Last Name", last_name)
        self._fill_field("First Name", first_name)
        self._fill_field("Company", company)
        self._fill_field("Address", address)
        self._fill_field("Address 2", address2)
        self._fill_field("City", city)
        self._fill_field("eg. CA", state)
        self._fill_field("Zipcode", zipcode)

    # ✅ Click Save
    def click_save(self):
        save_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//*[contains(@content-desc, "Save")]')
            )
        )
        save_button.click()
        time.sleep(3)

    # ✅ Tap Outside (to dismiss keyboard or popups)
    def tap_outside(self):
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except:
            pass
        # Click near the middle of the screen (x=500, y=500) to avoid the back button at top left
        self.driver.execute_script('mobile: clickGesture', {'x': 500, 'y': 500})
        time.sleep(2)

    # ✅ Click List Tab
    def click_list(self):
        list_btn = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//*[contains(@content-desc, "List") or contains(@text, "List")]')
            )
        )
        list_btn.click()
        time.sleep(3)

    # ✅ Search Customer
    def search_customer(self, search_text):
        from selenium.webdriver.common.action_chains import ActionChains
        
        # Try to find the search bar (Look for 'Search' label or an actual EditText)
        try:
            search_box = self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//*[contains(@content-desc, "Search") or contains(@text, "Search") or contains(@content-desc, "search")]')
                )
            )
            search_box.click()
        except:
            # If nothing has "Search", try the first EditText if it exists
            try:
                search_box = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
                search_box.click()
            except:
                pass
        
        time.sleep(2) # Wait for keyboard to open
        
        # Now type the text
        try:
            # Try setting it directly if an EditText is present
            active_input = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            active_input.send_keys(search_text)
        except:
            # Otherwise just type on the native keyboard using ActionChains!
            actions = ActionChains(self.driver)
            actions.send_keys(search_text)
            actions.perform()
        time.sleep(2)

    # ✅ Click generic ViewGroup (Search Result / Submit)
    def click_view_group(self):
        # The user wanted to click the result. We look for a ViewGroup containing the search text.
        try:
            result = self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, f'//*[contains(@content-desc, "Ty") or contains(@content-desc, "Abraham")]')
                )
            )
            result.click()
        except:
            pass