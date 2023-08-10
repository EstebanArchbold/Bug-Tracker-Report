import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TesBalanceEnquiry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://www.demo.guru99.com/V4/")
        cls.login(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def login(cls, driver):
        driver.find_element(By.NAME, "uid").send_keys("mngr517726")
        driver.find_element(By.NAME, "password").send_keys("Yvuzygu")
        driver.find_element(By.NAME, "btnLogin").click()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def test_VerifyAccountNumber_BE1(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        self.accept_alert()
        time.sleep(1)

    def test_VerifyAccountNumber_BE2(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        self.accept_alert()
        time.sleep(1)
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.accept_alert()
        time.sleep(2)
        
    def test_VerifyAccountNumber_BE3(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("!@#")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)

    def test_VerifyAccountNumber_BE4(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.SPACE)
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)

        time.sleep(2)

    def test_VerifySubmitButton_BE5(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("125319")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)

    def test_VerifySubmitButton_BE6(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("111111")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)

    def test_VerifySubmitButton_BE7(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.accept_alert()
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("123456")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        self.accept_alert()

if __name__ == "__main__":
    unittest.main()