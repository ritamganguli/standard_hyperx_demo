import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time

# Replace with your LambdaTest credentials
username = "gchawhan10"
access_key = "e0LlLtwPOwFxS1RcCyuenLu8vmO6Xpl3vO0Ppx4lNqiAuQBPYU"

# Set up Chrome options and LambdaTest capabilities
options = ChromeOptions()

lt_options = {
    "browserName": "MicrosoftEdge",
    "browserVersion": "dev",
    "platformName": "Windows 10",
    "username": username,
    "accessKey": access_key,
    "video": True,
    "resolution": "1920x1080",
    "network": True,
    "build": "test_build",
    "project": "unit_testing",
    "smartUI.project": "Dalbiiiiiiiir",
    "selenium_version": "4.0.0",
    "w3c": True,
    "plugin": "python-python"
}

options.set_capability("LT:Options", lt_options)

# Define the test case class
class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        # Connect to LambdaTest Remote WebDriver
        self.driver = webdriver.Remote(
            command_executor=f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub",
            options=options
        )

    def test_demo_site(self):
        driver = self.driver
        driver.maximize_window()

        # Correct navigation to the online demo site for LambdaTest
        driver.get("https://the-internet.herokuapp.com/download")
        
        # Click the link to download the PDF
        driver.find_element(By.XPATH, "//a[text()='sample.pdf']").click()
        time.sleep(1000000000000)  # Wait for the download to complete

    def tearDown(self):
        # Close the browser session
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
