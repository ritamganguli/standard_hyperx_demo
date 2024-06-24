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
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        driver.execute_script("arguments[0].click();", login_button)
        print("Logging in")
        time.sleep(35)

        print("Going over to a real-time session")
        real_time_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[2]")))
        driver.execute_script("arguments[0].click();", real_time_session)
        time.sleep(20)
        print("Went into real device session")

        print("Selecting browser_version")
        browser_version = self.wait.until(EC.element_to_be_clickable((By.ID, "version_126")))
        driver.execute_script("arguments[0].click();", browser_version)
        time.sleep(10)

        start_new_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", start_new_session)
        print("Starting a manual desktop session")
        time.sleep(15)
        
        end_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='aside__menu__link__anchor_new'])[13]")))
        driver.execute_script("arguments[0].click();", end_session)
        print("Starting a manual desktop session")
        time.sleep(30)

        print("Closing the real-time desktop session")
        end_real_time_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        driver.execute_script("arguments[0].click();", end_real_time_session)
        time.sleep(30)

        virtual_mobile = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[text()='Virtual Mobile'])[1]")))
        driver.execute_script("arguments[0].click();", virtual_mobile)
        print("Trying manual session over simulator/browser")
        time.sleep(20)

        virtual_mobile_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
        driver.execute_script("arguments[0].click();", virtual_mobile_input)
        time.sleep(10)

        start_virtual_mobile_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", start_virtual_mobile_session)
        print("Starting manual session of emulator...")
        time.sleep(45)

        driver.navigate().back()

        # end_virtual_mobile_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='End Session']")))
        # driver.execute_script("arguments[0].click();", end_virtual_mobile_session)
        print("Ending session")

        # confirm_end_virtual_mobile_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        # driver.execute_script("arguments[0].click();", confirm_end_virtual_mobile_session)
        print("Exiting from the device")

        main_page = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']")))
        driver.execute_script("arguments[0].click();", main_page)
        print("Going back to the main page")
        time.sleep(20)

        print("Picking up real device")
        real_device = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[3]")))
        driver.execute_script("arguments[0].click();", real_device)
        time.sleep(60)

        print("Starting session over android real device")
        start_android_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", start_android_session)
        time.sleep(30)

        end_android_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='End Session']")))
        driver.execute_script("arguments[0].click();", end_android_session)
        print("Ending session")

        confirm_end_android_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        driver.execute_script("arguments[0].click();", confirm_end_android_session)
        print("Ended the session")
        time.sleep(30)

        ios_device = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='osSelectorHeader flex']/div/span[2]")))
        driver.execute_script("arguments[0].click();", ios_device)
        print("Selected ios device")
        time.sleep(10)

        print("Starting session over ios real device")
        start_ios_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", start_ios_session)
        time.sleep(60)

        end_ios_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='End Session']")))
        driver.execute_script("arguments[0].click();", end_ios_session)
        print("Ending session")

        confirm_end_ios_session = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']")))
        driver.execute_script("arguments[0].click();", confirm_end_ios_session)
        print("Ended the session")
        time.sleep(30)

        main_page_again = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']")))
        driver.execute_script("arguments[0].click();", main_page_again)
        print("Going back to the main page")
        time.sleep(15)

        print("Going to automation")
        web_automation = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]")))
        driver.execute_script("arguments[0].click();", web_automation)
        time.sleep(25)

        print("Currently inside web automation")
        web_automation_again = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]")))
        driver.execute_script("arguments[0].click();", web_automation_again)
        print("Now going to app automation")

        app_automation = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='App Automation']")))
        driver.execute_script("arguments[0].click();", app_automation)
        time.sleep(15)

        main_page_third_time = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']")))
        driver.execute_script("arguments[0].click();", main_page_third_time)
        print("Going back to the main page")

        more_tools = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[9]")))
        driver.execute_script("arguments[0].click();", more_tools)
        print("Going over more tools")
        time.sleep(20)

        integration_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='aside__menu__bottom__submenu__item__icon']")))
        driver.execute_script("arguments[0].click();", integration_icon)

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

        integration_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='ltch-aside-menu-bottom-submenu-item-wrapper']/li[1]/a[1]")))
        driver.execute_script("arguments[0].click();", integration_link)
        time.sleep(30)
        print("Ending the test...")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
