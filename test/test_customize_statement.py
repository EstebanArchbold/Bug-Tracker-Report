from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCustomizedStatement(unittest.TestCase):
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

    def account(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("125344")    

    def accept_alert(self):
        self.driver.switch_to.alert.accept()    
    

if __name__ == "__main__":
    unittest.main()