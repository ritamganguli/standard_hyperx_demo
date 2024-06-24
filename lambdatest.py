import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key
sign_in_mail=os.getenv("sign_in_mail")
password=os.getenv("password")

# username = "shubhamr"  # Replace the username
# access_key = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"  # Replace the access key


# paste your capibility options below

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "win10"
lt_options = {}
lt_options["username"] = username
lt_options["accessKey"] = access_key
lt_options["video"] = True
lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["build"] = "test_build"
lt_options["project"] = "unit_testing"
lt_options["smartUI.project"] = "test"
lt_options["name"] = "basic_unit_selinium"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability("LT:Options", lt_options)


# Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
# Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
# Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
# Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot
# Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/


class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    # """ You can write the test cases here """
    def test_demo_site(self):
        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get(
            "https://accounts.lambdatest.com/login"
        )

        # Let's click on a element
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
        print("Going over to a real time session")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[2]").click()
        time.sleep(20)
        print("Went into real device session")
        #driver.find_element(By.XPATH, "//div[text()='Windows 10']").click()
        #print("Selected windows 10")
        print("Selecting browser_version")
        driver.find_element(By.XPATH,"//div[@id='version_126']").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"//span[text()='Start']/parent::span/parent::button").click()
        print("Staring a manual desktop session")
        time.sleep(15)
        driver.find_element(By.XPATH,"(//div[@class='aside__menu__link aside__menu__link__anchor_new'])[13]").click()
        time.sleep(30)
        print("Clsoing the real time desktop session")
        driver.find_element(By.XPATH,"//span[text()='Yes, End Session']").click()
        time.sleep(30)
        driver.find_element(By.XPATH,"(//span[text()='Virtual Mobile'])[1]").click()
        print("Trying manual session over simulatour/browser")
        time.sleep(20)
        driver.find_element(By.XPATH,"//input[@type='text']").click()
        #driver.find_element(By.XPATH,"//input[@type='text']").send_key("https://automation.lambdatest.com/build?&statusTab=All")
        time.sleep(10)
        driver.find_element(By.XPATH,"//span[text()='Start']/parent::span/parent::button").click()
        print("Starting manual seesion of emulatour......")
        time.sleep(45)
        driver.find_element(By.XPATH,"(//span[text()='End Session'])[1]").click()
        print("Ending session")
        driver.find_element(By.XPATH,"//span[text()='Yes, End Session']").click()
        print("Exciting from the device")
        driver.find_element(By.XPATH,"//div[@class='aside__menu__link aside__menu__link__anchor']").click()
        print("Going back to the main page")
        time.sleep(20)
        print("picking up real device")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[3]").click()
        time.sleep(60)
        print("starting session over android real device")
        driver.find_element(By.XPATH,"//span[text()='Start']/parent::span/parent::span/parent::button").click()
        time.sleep(30)
        driver.find_element(By.XPATH,"(//span[text()='End Session'])[1]").click()
        print("Ending session")
        driver.find_element(By.XPATH,"//span[text()='Yes, End Session']").click()
        print("Ended the session")
        time.sleep(30)
        driver.find_element(By.XPATH,"//div[@class='osSelectorHeader flex']/div/span[2]").click()
        print("Selected ios device")
        time.sleep(10)
        print("starting session over ios real device")
        driver.find_element(By.XPATH,"//span[text()='Start']/parent::span/parent::span/parent::button").click()
        time.sleep(60)
        driver.find_element(By.XPATH,"(//span[text()='End Session'])[1]").click()
        print("Ending session")
        driver.find_element(By.XPATH,"//span[text()='Yes, End Session']").click()
        print("Ended the session")
        time.sleep(30)
        driver.find_element(By.XPATH,"//div[@class='aside__menu__link aside__menu__link__anchor']").click()
        print("Going back to the main page")
        time.sleep(15)
        print("Going to automation")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]").click()
        time.sleep(25)
        print("print curently inside web automation")
        driver.find_element(By.XPATH, "//div[@id='left_sidebar_header-items']/nav/ul/li[4]").click()
        print("Now going to app automation")
        driver.find_element(By.XPATH, "(//span[text()='App Automation'])[1]").click()
        time.sleep(15)
        driver.find_element(By.XPATH,"//div[@class='aside__menu__link aside__menu__link__anchor']").click()
        print("Going back to the main page")
        driver.find_element(By.XPATH,"//div[@id='left_sidebar_header-items']/nav/ul/li[9]").click()
        print("Going over more tools")
        time.sleep(20)
        driver.find_element(By.XPATH,"(//span[@class='aside__menu__bottom__submenu__item__icon'])[3]").click()
        print("Going over integration")
        time.sleep(10)
        driver.find_element(By.XPATH,"//ul[@class='ltch-aside-menu-bottom-submenu-item-wrapper']/li[1]/a[1]").click()
        time.sleep(30)
        print("Ending the test........")























        # location = driver.find_element(By.NAME, "li2")
        # location.click()
        # print("Clicked on the second element")

        # # Take Smart UI screenshot
        # # driver.execute_script("smartui.takeScreenshot")

        # # Let's add a checkbox
        # driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        # add_button = driver.find_element(By.ID, "addbutton")
        # add_button.click()
        # print("Added LambdaTest checkbox")

        # # print the heading
        # search = driver.find_element(By.CSS_SELECTOR, ".container h2")
        # assert search.is_displayed(), "heading is not displayed"
        # print(search.text)
        # search.click()
        # driver.implicitly_wait(3)

        # # Let's download the invoice
        # heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        # if heading.is_displayed():
        #     heading.click()
        #     driver.execute_script("lambda-status=passed")
        #     print("Tests are run successfully!")
        # else:
        #     driver.execute_script("lambda-status=failed")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
