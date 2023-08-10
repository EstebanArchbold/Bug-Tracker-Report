import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestNewAccount(unittest.TestCase):
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
    def profile(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("61897")
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def test_VerifyCustomerID_NA1(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(3)
    
    def test_VerifyCustomerID_NA2(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        time.sleep(3)
        self.driver.refresh()

    def test_VerifyCustomerID_NA3(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        time.sleep(3)
        self.driver.refresh()

    def test_VerifyCustomerID_NA4(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()        
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(3)
        self.driver.refresh()

    def test_VerifyCustomerID_NA5(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" 12345")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(3)
        self.driver.refresh()

    def test_VerifyInitialDeposit_NA6(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" 123456")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(3)
        self.driver.refresh()

    def test_VerifyInitialDeposit_NA7(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "cusid").clear()
        time.sleep(2)
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.refresh()

    def test_VerifyInitialDeposit_NA8(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.refresh()

    def test_VerifyInitialDeposit_NA9(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.refresh()

    def test_VerifyInitialDeposit_NA10(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" 12345")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.refresh()
    
    def test_VerifyAccounttypeDropdown_NA11(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Savings']").click()
        time.sleep(2)
        self.driver.refresh()

    def test_VerifyAccounttypeDropdown_NA12(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Current']").click()
        time.sleep(2)
        self.driver.refresh()
    
    def test_ResetButton_NA13(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("61897")
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Savings']").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("61897")
        time.sleep(2)
        self.driver.find_element(By.NAME, "reset").click()
        self.driver.refresh()
    
    def test_SubmitButton_NA14(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Savings']").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("10234")
        time.sleep(2)
        self.driver.find_element(By.NAME, "button2").click()
        self.accept_alert()
        time.sleep(2)
        self.driver.refresh()

    def test_SubmitButton_NA15(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("61897")
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Savings']").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("10234")
        time.sleep(2)
        self.driver.find_element(By.NAME, "button2").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Continue").click()
