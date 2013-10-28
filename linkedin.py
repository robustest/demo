from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Linkedin(unittest.TestCase):
    
    desired_capabilities = {
                "browserName": "firefox",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=Linkedin.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.linkedin.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_home(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual("", driver.find_element_by_css_selector("img.logo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("session_key-login").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("session_password-login").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("session_password-login").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("firstName-coldRegistrationForm").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("lastName-coldRegistrationForm").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("email-coldRegistrationForm").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("password-coldRegistrationForm").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Join now", driver.find_element_by_id("btn-submit").get_attribute("value"))
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
