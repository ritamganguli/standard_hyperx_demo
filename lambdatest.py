import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.wait = WebDriverWait(self.driver, 30)  # Define WebDriverWait

    def test_demo_site(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get("https://accounts.lambdatest.com/login")

        time.sleep(15)  # Wait for the page to load

        print("Entering Mail To Log in")
        self.wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(sign_in_mail)
        print("Entering Password")
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        time.sleep(7)
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        driver.execute_script("document.getElementById('login-button').click();")
        print("Logging in")
        time.sleep(35)

        print("Going over to a real-time session")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[2]")))
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(2)').click();")
        time.sleep(20)
        print("Went into real device session")

        print("Selecting browser_version")
        self.wait.until(EC.element_to_be_clickable((By.ID, "version_126")))
        driver.execute_script("document.getElementById('version_126').click();")
        time.sleep(10)

        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", element)
        print("Starting a manual desktop session")
        time.sleep(15)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='aside__menu__link__anchor_new'])[13]")))
        driver.execute_script("document.querySelectorAll('.aside__menu__link__anchor_new')[12].click();")
        time.sleep(30)

        print("Closing the real-time desktop session")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        time.sleep(30)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[text()='Virtual Mobile'])[1]")))
        driver.execute_script("document.querySelector('span:textContains(Virtual Mobile)').click();")
        print("Trying manual session over simulator/browser")
        time.sleep(20)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
        driver.execute_script("document.querySelector('input[type=text]').click();")
        time.sleep(10)

        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", element)
        print("Starting manual session of emulator...")
        time.sleep(45)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='End Session']")))
        driver.execute_script("document.querySelector('span:textContains(End Session)').click();")
        print("Ending session")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        print("Exiting from the device")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']")))
        driver.execute_script("document.querySelector('.aside__menu__link__anchor').click();")
        print("Going back to the main page")
        time.sleep(20)

        print("Picking up real device")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[3]")))
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(3)').click();")
        time.sleep(60)

        print("Starting session over android real device")
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(30)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='End Session']")))
        driver.execute_script("document.querySelector('span:textContains(End Session)').click();")
        print("Ending session")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        print("Ended the session")
        time.sleep(30)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='osSelectorHeader flex']/div/span[2]")))
        driver.execute_script("document.querySelector('.osSelectorHeader .flex span:nth-child(2)').click();")
        print("Selected ios device")
        time.sleep(10)

        print("Starting session over ios real device")
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(60)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='End Session']")))
        driver.execute_script("document.querySelector('span:textContains(End Session)').click();")
        print("Ending session")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        driver.execute_script("document.querySelector('span:textContains(Yes, End Session)').click();")
        print("Ended the session")
        time.sleep(30)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']")))
        driver.execute_script("document.querySelector('.aside__menu__link__anchor').click();")
        print("Going back to the main page")
        time.sleep(15)

        print("Going to automation")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]")))
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(4)').click();")
        time.sleep(25)

        print("Currently inside web automation")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]")))
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(4)').click();")
        print("Now going to app automation")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='App Automation']")))
        driver.execute_script("document.querySelector('span:textContains(App Automation)').click();")
        time.sleep(15)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']")))
        driver.execute_script("document.querySelector('.aside__menu__link__anchor').click();")
        print("Going back to the main page")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[9]")))
        driver.execute_script("document.querySelector('#left_sidebar_header-items nav ul li:nth-child(9)').click();")
        print("Going over more tools")
        time.sleep(20)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='aside__menu__bottom__submenu__item__icon']")))
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

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='ltch-aside-menu-bottom-submenu-item-wrapper']/li[1]/a[1]")))
        driver.execute_script("document.querySelector('.ltch-aside-menu-bottom-submenu-item-wrapper li a').click();")
        time.sleep(30)
        print("Ending the test...")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
