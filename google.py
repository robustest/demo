from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Google(unittest.TestCase):
    
    desired_capabilities = {
                "browserName": "firefox",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=Google.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.co.in"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search_fail(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual("India", driver.find_element_by_id("hplogo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("gbqfq").send_keys("facebook")
        driver.find_element_by_name("btnG").click()
        try: self.assertEqual("You cant find twitter in Facebook search", driver.find_element_by_link_text("Welcome to Facebook - Log In, Sign Up or Learn More").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def test_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual("India", driver.find_element_by_id("hplogo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("gbqfq").send_keys("robustest.com")
        driver.find_element_by_name("btnG").click()
        try: self.assertEqual("RobusTest - Best Automation Testing Framework", driver.find_element_by_link_text("RobusTest - Best Automation Testing Framework").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("em").click()
        try: self.assertEqual("Robustest", driver.find_element_by_css_selector("small").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Register", driver.find_element_by_id("signup").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Features", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Enterprise", driver.find_element_by_css_selector("li.purple > a.dropdown-toggle > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_link_text("Help").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Login", driver.find_element_by_css_selector("li.light-orange > a.dropdown-toggle > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("As Easy as", driver.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[5]/a/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
