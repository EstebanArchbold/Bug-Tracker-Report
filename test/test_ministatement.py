from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestMiniStatement(unittest.TestCase):
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
    
    def test_mS1(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
    def test_mS2(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        time.sleep(3)
    def test_mS3(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("!@#")
        time.sleep(3)
    def test_mS4(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
    def test_mS5(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" L")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
    def test_mS6(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.account()
        self.driver.find_element(By.NAME, "AccSubmit").click()   
        time.sleep(3)
    def test_mS7(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.switch_to.alert.accept()   
        time.sleep(3)
    def test_mS8(self):
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer")
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123456")      
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()