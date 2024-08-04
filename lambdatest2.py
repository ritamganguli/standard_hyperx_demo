import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

username = "shubhamr"  # Replace with your username
access_key = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"  # Replace with your access key

# Setting up the Chrome options and LambdaTest capabilities
options = ChromeOptions()
options.browser_version = "126.0"
options.platform_name = "win11"

lt_options = {
    "username": username,
    "accessKey": access_key,
    "video": True,
    "resolution": "1920x1080",
    "network": True,
    "build": "test_build",
    "project": "unit_testing",
    "smartUI.project": "stemcell_trail_1",
    "selenium_version": "4.0.0",
    "w3c": True,
    "plugin": "python-python"
}

options.set_capability("LT:Options", lt_options)

# Define the test case class
class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub",
            options=options
        )

    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Load URL
        print("Loading URL")
        driver.get("https://egift.laura.ca/gifter/digital")
        driver.maximize_window()

        # Scroll to specific coordinates
        driver.execute_script("window.scrollTo(63, 1566)")

        # Execute SmartUI screenshot
        driver.execute_script("smartui.takeFullPageScreenshot='Ritam1'")
        time.sleep(30)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
