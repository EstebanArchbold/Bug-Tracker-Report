import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestDeleteCustomer(unittest.TestCase):
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
        self.driver.find_element(By.NAME, "cusid").send_keys("12345")

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def test_VerifyAccountNumber_customer_DA1(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(3)

    def test_VerifyAccountNumber_customer_DA2(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("12345")
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        time.sleep(3)
        self.driver.refresh()
    
    def test_VerifyAccountNumber_customer_DA3(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        time.sleep(3)
        self.driver.refresh()

    def test_VerifyAccountNumber_customer_DA4(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()        
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        time.sleep(3)
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        self.driver.refresh()

    def test_VerifyAccountNumber_customer_DA5(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" 12345")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(3)
        self.driver.refresh()

    def test_Submit_Button_DA6(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(1)
        self.accept_alert()
        self.driver.refresh()

    def test_Submit_Button_DA7(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("77523")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)
        self.accept_alert()
        self.driver.refresh()

    def test_Reset_Button_DA8(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("qwer      ")
        time.sleep(2)
        self.driver.find_element(By.NAME, "res").click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        time.sleep(2) 
        self.driver.find_element(By.NAME, "res").click()
        self.driver.refresh()
        time.sleep(2)

    
if __name__ == "__main__":
    unittest.main()