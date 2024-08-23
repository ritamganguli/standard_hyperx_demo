import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
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
    "smartUI.project": "Dalbiiiiiiiir",
    "selenium_version": "4.0.0",
    "tunnel": True,
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
        driver.maximize_window()
        driver.get("https://egift.laura.ca/gifter/digital")

        # Execute JavaScript to get the zoom level
        zoom_level = driver.execute_script("return window.devicePixelRatio;")

        print(zoom_level)
        
        # Assert that zoom level is either 2 or 1
        self.assertIn(zoom_level, [1], f"Zoom level is {zoom_level}, expected 1 or 2")
        
        # Take a full-page screenshot with Smart UI
        driver.execute_script("smartui.takeFullPageScreenshot=Dalbir1")

        self.assertIn(zoom_level, [1], f"Zoom level is {zoom_level}, expected 1 or 2")
        
        # Wait for 30 seconds to capture any asynchronous processes
        time.sleep(30)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
