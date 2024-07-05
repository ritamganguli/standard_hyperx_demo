import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = "shubhamr"
access_key = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"
sign_in_mail = "shubhamr@lambdatest.com"
password = "Gmail@12345"
build = os.getenv("LT_BUILD_NAME")

# Define mobile emulation settings
mobile_emulation = {
    "deviceName": "iPhone X"  # You can change this to any device you want to emulate
}

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "win10"
lt_options = {}
lt_options["username"] = username
lt_options["accessKey"] = access_key
lt_options["video"] = True
lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["smartWait"] = 60
lt_options["build"] = build
lt_options["project"] = "unit_testing"
lt_options["name"] = "basic_unit_selenium"
lt_options["w3c"] = True
lt_options["accessibility"] = True,
lt_options["accessibility.wcagVersion"] = "wcag21a",
lt_options["accessibility.needsReview"] = True,
lt_options["plugin"] = "python-python"
options.set_capability("LT:Options", lt_options)

# Add mobile emulation to ChromeOptions
options.add_experimental_option("mobileEmulation", mobile_emulation)

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

        print("Loading URL")
        driver.get("https://accounts.lambdatest.com/login")

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
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[2]").click()
        time.sleep(20)
        print("Went into real device session")
        print("Selecting browser_version")
        driver.find_element(By.XPATH, "//div[@id='version_126']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//span[text()='Start']/parent::span/parent::button").click()
        print("Starting a manual desktop session")
        time.sleep(15)
        driver.find_element(By.XPATH, "(//div[@class='aside__menu__link aside__menu__link__anchor_new'])[13]").click()
        time.sleep(30)
        print("Closing the real-time desktop session")
        driver.find_element(By.XPATH, "//span[text()='Yes, End Session']").click()
        time.sleep(30)
        driver.find_element(By.XPATH, "(//span[text()='Virtual Mobile'])[1]").click()
        print("Trying manual session over simulator/browser")
        time.sleep(20)
        driver.find_element(By.XPATH, "//input[@type='text']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//span[text()='Start']/parent::span/parent::button").click()
        print("Starting manual session of emulator......")
        time.sleep(45)
        driver.find_element(By.XPATH, "(//span[text()='End Session'])[1]").click()
        print("Ending session")
        driver.find_element(By.XPATH, "//span[text()='Yes, End Session']").click()
        print("Exiting from the device")
        driver.find_element(By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']").click()
        print("Going back to the main page")
        time.sleep(20)
        print("Picking up real device")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[3]").click()
        time.sleep(60)
        print("Starting session over Android real device")
        driver.find_element(By.XPATH, "//span[text()='Start']/parent::span/parent::span/parent::button").click()
        time.sleep(30)
        driver.find_element(By.XPATH, "(//span[text()='End Session'])[1]").click()
        print("Ending session")
        driver.find_element(By.XPATH, "//span[text()='Yes, End Session']").click()
        print("Ended the session")
        time.sleep(30)
        driver.find_element(By.XPATH, "//div[@class='osSelectorHeader flex']/div/span[2]").click()
        print("Selected iOS device")
        time.sleep(10)
        print("Starting session over iOS real device")
        driver.find_element(By.XPATH, "//span[text()='Start']/parent::span/parent::span/parent::button").click()
        time.sleep(60)
        driver.find_element(By.XPATH, "(//span[text()='End Session'])[1]").click()
        print("Ending session")
        driver.find_element(By.XPATH, "//span[text()='Yes, End Session']").click()
        print("Ended the session")
        time.sleep(30)
        driver.find_element(By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']").click()
        print("Going back to the main page")
        time.sleep(15)
        print("Going to automation")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]").click()
        time.sleep(25)
        print("Currently inside web automation")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]").click()
        print("Now going to app automation")
        driver.find_element(By.XPATH, "(//span[text()='App Automation'])[1]").click()
        time.sleep(15)
        driver.find_element(By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']").click()
        print("Going back to the main page")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[9]").click()
        print("Going over more tools")
        time.sleep(20)
        driver.find_element(By.XPATH, "(//span[@class='aside__menu__bottom__submenu__item__icon'])[3]").click()
        print("Going over integration")
        time.sleep(10)
        driver.find_element(By.XPATH, "//ul[@class='ltch-aside-menu-bottom-submenu-item-wrapper']/li[1]/a[1]").click()
        time.sleep(30)
        for i in range(600):
            try:
                element = driver.find_element(By.XPATH, "(//span[@class='aside__menu__bottom__submenu__item__icon'])[3]")
                if element.is_displayed():
                    print(f"Element is displayed in iteration {i}")
                else:
                    print(f"Element is not displayed in iteration {i}")
            except:
                print("exception")
        print("Ending the test........")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
