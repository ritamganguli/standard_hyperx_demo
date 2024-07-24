import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key
sign_in_mail=os.getenv("sign_in_mail")
password=os.getenv("password")
build=os.getenv("LT_BUILD_NAME")

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "win10"
lt_options = {}
lt_options["username"] = username
lt_options["accessKey"] = access_key
lt_options["video"] = True
lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["smartWait"]= 60
lt_options["build"] = build
lt_options["name"] = "basic_unit_selenium"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability("LT:Options", lt_options)


class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub",
            options=options,
        )
        self.wait = WebDriverWait(self.driver, 60)

    def test_demo_site(self):
        driver = self.driver
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get("https://accounts.lambdatest.com/login")

        # Let's click on an element
        print("Entering Mail To Log in")
        self.wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(sign_in_mail)
        print("Entering Password")
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        print("Logging in")

        print("Going over to a real-time session")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[2]"))).click()
        print("Went into real device session")

        print("Selecting browser_version")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='version_126']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Start']/parent::span/parent::button"))).click()
        print("Starting a manual desktop session")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='aside__menu__link aside__menu__link__anchor_new'])[13]"))).click()
        print("Closing the real-time desktop session")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[text()='Virtual Mobile'])[1]"))).click()
        print("Trying manual session over simulator/browser")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).click()
        time.sleep(5)
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Start New Session']")))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(60)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[text()='End Session'])[1]"))).click()
        print("Ending session")
        time.sleep(7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']"))).click()
        print("Exiting from the device")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']"))).click()
        print("Going back to the main page")

        print("Picking up real device")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[3]"))).click()
        print("Starting session over Android real device")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='public-device-list']/ul/li[3]"))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Start']/parent::span/parent::span/parent::button"))).click()
        time.sleep(50)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='endsession']"))).click()
        print("Ending session")
        time.sleep(7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']"))).click()

        print("Selecting iOS device")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='osSelectorHeader flex']/div/span[2]"))).click()
        print("Starting session over iOS real device")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='public-device-list']/ul/li[3]"))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Start']/parent::span/parent::span/parent::button"))).click()
        time.sleep(50)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='endsession']"))).click()
        print("Ending session")
        time.sleep(7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Yes, End Session']"))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']"))).click()
        print("Going back to the main page")
        time.sleep(10)
        print("Going to automation")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]"))).click()
        print("Currently inside web automation")
        time.sleep(5)
        print("Now going to app automation")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[text()='App Automation'])[1]"))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='aside__menu__link aside__menu__link__anchor']"))).click()
        print("Going back to the main page")

        print("Going over more tools")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[9]"))).click()

        print("Going over integration")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='aside__menu__bottom__submenu__item__icon'])[3]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='ltch-aside-menu-bottom-submenu-item-wrapper']/li[1]/a[1]"))).click()
        for i in range(600):
            try:
                element = driver.find_element(By.XPATH, "(//span[@class='aside__menu__bottom__submenu__item__icon'])[3]")
                if element.is_displayed():
                    print(f"Element is displayed in iteration {i}")
                else:
                    print(f"Element is not displayed in iteration {i}")
            except: 
                print("exception")
        time.sleep(15)
        print("Ending the test........")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
