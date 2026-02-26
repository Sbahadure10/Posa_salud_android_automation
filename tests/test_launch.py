from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import time


def test_launch_android_app():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    # Explicit package + activity
    options.app_package = "com.posanywhere.salud"
    options.no_reset = True
    options.dont_stop_app_on_reset = True
    options.auto_launch = False

    # APK path
    app_path = os.path.abspath("apps/app-release.apk")
    options.app = app_path

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    time.sleep(10)

    driver.quit()