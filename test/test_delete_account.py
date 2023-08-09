import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TesDeleteCustomer(unittest.TestCase):
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

    def test_VerifyAccountNumber_DA1(self):
        
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "accountno")
        self.driver.find_element(By.NAME, "AccSubmit").click()

    def test_VerifyAccountNumber_DA2(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        self.accept_alert()
        time.sleep(1)
        self.accept_alert()
        time.sleep(1)
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        self.accept_alert()
        time.sleep(2)
        
    def test_VerifyAccountNumber_DA3(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
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

    def test_VerifyAccountNumber_DA4(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)

    def test_VerifyAccountNumber_DA5(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.SPACE)
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(2)

    def test_VerifyAccountNumber_DA6(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("125319")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        




        
        

    


        


        


     
    

if __name__ == "__main__":
    unittest.main()
 