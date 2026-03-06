from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import time


def launch_android_app():

    options = UiAutomator2Options()

    # Device configuration
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    # App configuration
    options.app_package = "com.posanywhere.salud"
    options.no_reset = True
    options.dont_stop_app_on_reset = True

    # APK path
    app_path = os.path.abspath("apps/app-release.apk")
    options.app = app_path

    # Start Appium session
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    print("App launched successfully")

    # Wait so you can see the app open
    time.sleep(10)

    # Close session
    driver.quit()


if __name__ == "__main__":
    launch_android_app()