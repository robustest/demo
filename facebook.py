from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Facebook(unittest.TestCase): 
    
    desired_capabilities = {
                "browserName": "firefox",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }
    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=Facebook.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.facebook.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_home(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual("", driver.find_element_by_css_selector("img.fb_logo.img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("email").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("pass").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Keep me logged in", driver.find_element_by_css_selector("label._5bb4 > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Log In", driver.find_element_by_id("loginbutton").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Welcome to Facebook", driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Connect with friends and the world around you.", driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("u_0_0").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("u_0_1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("u_0_2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("u_0_3").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("u_0_4").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Birthday", driver.find_element_by_css_selector("div._58mr.lfloat").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Sign Up for Facebook", driver.find_element_by_id("u_0_5").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Terms", driver.find_element_by_link_text("Terms").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Data Use Policy", driver.find_element_by_link_text("Data Use Policy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Cookie Use", driver.find_element_by_link_text("Cookie Use").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Stay in touch", driver.find_element_by_xpath("//div[@id='content']/div/div/div[2]/table/tbody/tr/td/div/div/div/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Get the latest", driver.find_element_by_xpath("//div[@id='content']/div/div/div[2]/table/tbody/tr/td[2]/div/div/div/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Share what's up with you", driver.find_element_by_xpath("//div[@id='content']/div/div/div[2]/table/tbody/tr/td[3]/div/div/div/div").text)
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