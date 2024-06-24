import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")
sign_in_mail = os.getenv("sign_in_mail")
password = os.getenv("password")
build = os.getenv("LT_BUILD_NAME")

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "win10"
lt_options = {
    "username": username,
    "accessKey": access_key,
    "video": True,
    "resolution": "1920x1080",
    "network": True,
    "build": build,
    "name": "basic_unit_selenium",
    "w3c": True,
    "plugin": "python-python"
}
options.set_capability("LT:Options", lt_options)


class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get("https://accounts.lambdatest.com/login")

        time.sleep(15)
        time.sleep(15)
        print("Entering Mail To Log in")
        driver.find_element(By.ID, "email").send_keys(sign_in_mail)
        time.sleep(7)
        print("Entering Password")
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(7)
        driver.find_element(By.ID, "login-button").click()
        print("Logging in")
        time.sleep(35)
        print("Going over to a real-time session")
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(2)').click();")
        time.sleep(20)
        print("Went into real device session")
        print("Selecting browser_version")
        driver.execute_script("document.getElementById('version_126').click();")
        time.sleep(10)
        driver.execute_script("document.querySelector('span:textContains(Start)').parentElement.click();")
        print("Starting a manual desktop session")
        time.sleep(15)
        driver.execute_script("document.querySelectorAll('.aside__menu__link__anchor_new')[12].click();")
        time.sleep(30)
        print("Closing the real-time desktop session")
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        time.sleep(30)
        driver.execute_script("document.querySelector('span:textContains(Virtual Mobile)').click();")
        print("Trying manual session over simulator/browser")
        time.sleep(20)
        driver.execute_script("document.querySelector('input[type=text]').click();")
        time.sleep(10)
        driver.execute_script("document.querySelector('span:textContains(Start)').parentElement.click();")
        print("Starting manual session of emulator...")
        time.sleep(45)
        driver.execute_script("document.querySelector('span:textContains(End Session)').click();")
        print("Ending session")
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        print("Exiting from the device")
        driver.execute_script("document.querySelector('.aside__menu__link__anchor').click();")
        print("Going back to the main page")
        time.sleep(20)
        print("Picking up real device")
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(3)').click();")
        time.sleep(60)
        print("Starting session over android real device")
        driver.execute_script("document.querySelector('span:textContains(Start)').parentElement.click();")
        time.sleep(30)
        driver.execute_script("document.querySelector('span:textContains(End Session)').click();")
        print("Ending session")
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        print("Ended the session")
        time.sleep(30)
        driver.execute_script("document.querySelector('.osSelectorHeader .flex span:nth-child(2)').click();")
        print("Selected ios device")
        time.sleep(10)
        print("Starting session over ios real device")
        driver.execute_script("document.querySelector('span:textContains(Start)').parentElement.click();")
        time.sleep(60)
        driver.execute_script("document.querySelector('span:textContains(End Session)').click();")
        print("Ending session")
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        print("Ended the session")
        time.sleep(30)
        driver.execute_script("document.querySelector('.aside__menu__link__anchor').click();")
        print("Going back to the main page")
        time.sleep(15)
        print("Going to automation")
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(4)').click();")
        time.sleep(25)
        print("Currently inside web automation")
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(4)').click();")
        print("Now going to app automation")
        driver.execute_script("document.querySelector('span:textContains(App Automation)').click();")
        time.sleep(15)
        driver.execute_script("document.querySelector('.aside__menu__link__anchor').click();")
        print("Going back to the main page")
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(9)').click();")
        print("Going over more tools")
        time.sleep(20)
        driver.execute_script("document.querySelectorAll('.aside__menu__bottom__submenu__item__icon')[2].click();")
        for i in range(600):
            try:
                element = driver.find_element(By.XPATH, "(//span[@class='aside__menu__bottom__submenu__item__icon'])[3]")
                if element.is_displayed():
                    print(f"Element is displayed in iteration {i}")
                else:
                    print(f"Element is not displayed in iteration {i}")
            except:
                print("Exception")
        print("Going over integration")
        time.sleep(10)
        driver.execute_script("document.querySelector('.ltch-aside-menu-bottom-submenu-item-wrapper li a').click();")
        time.sleep(30)
        print("Ending the test...")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
