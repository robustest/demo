from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Twitter(unittest.TestCase):
    
    desired_capabilities = {
                "browserName": "firefox",
                "platform":"LINUX",
                "hubUrl" : "http://127.0.0.1:4444/wd/hub"
                }

    
    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=Twitter.desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "https://twitter.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_home(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual("Twitter", driver.find_element_by_css_selector("span.icon.bird-topbar-blue").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Language:", driver.find_element_by_css_selector("small").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual("Welcome to Twitter.", driver.find_element_by_css_selector("h1").text)
        self.assertEqual("Start a conversation, explore your interests, and be in the know.", driver.find_element_by_css_selector("div.callout-copy > p").text)
        try: self.assertEqual("Download on the App Store", driver.find_element_by_link_text("Download on the App Store").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Android app on Google play", driver.find_element_by_link_text("Android app on Google play").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("View other devices", driver.find_element_by_link_text("View other devices").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Username or email", driver.find_element_by_css_selector("label.placeholder").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Password", driver.find_element_by_xpath("//div[@id='front-container']/div[2]/div[2]/form/table/tbody/tr/td/div/label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Sign in", driver.find_element_by_xpath("(//button[@type='submit'])[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Remember me", driver.find_element_by_css_selector("div.remember-forgot > label.remember > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Sign up for Twitter", driver.find_element_by_css_selector("button.btn.signup-btn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("About", driver.find_element_by_link_text("About").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_link_text("Help").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Blog", driver.find_element_by_link_text("Blog").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Status", driver.find_element_by_link_text("Status").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Jobs", driver.find_element_by_link_text("Jobs").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Ads", driver.find_element_by_link_text("Ads").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Terms", driver.find_element_by_link_text("Terms").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Privacy", driver.find_element_by_link_text("Privacy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Advertisers", driver.find_element_by_link_text("Advertisers").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Businesses", driver.find_element_by_link_text("Businesses").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Media", driver.find_element_by_link_text("Media").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Developers", driver.find_element_by_link_text("Developers").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Resources", driver.find_element_by_link_text("Resources").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Directory", driver.find_element_by_link_text("Directory").text)
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
