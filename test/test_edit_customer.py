# edit_customer_test.py
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestEditCustomerCreation(unittest.TestCase):
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

    def test_eC1(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(3)
    
    def test_eC2(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        
        time.sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        
        time.sleep(3)

    def test_eC3(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        
        time.sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        
        time.sleep(3)

    def test_eC4(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        # self.driver.find_element(By.NAME, "cusid").send_keys("27327")
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(3)

    def test_eC5(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").clear()
        self.driver.find_element(By.NAME, "addr").send_keys("")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").clear()
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        time.sleep(3)

    def test_eC6(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys("")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        time.sleep(3)

    def test_eC7(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys("1234")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys("city123")
        time.sleep(3)


    def test_eC8(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys("City!@#")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys("!@#")
        time.sleep(3)

    def test_eC9(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").send_keys(" ")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        time.sleep(3)

    def test_eC10(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").send_keys("1234")
        time.sleep(3)
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").send_keys("State123")
        time.sleep(3)

    def test_eC11(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").send_keys("State!@#")
        time.sleep(3)
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").send_keys("!@#")
        time.sleep(3)
        self.driver.refresh()

    def test_eC12(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234PIN")
        time.sleep(3)

    def test_eC13(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys(" ")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        time.sleep(3)

    def test_eC14(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234567")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("123")
        time.sleep(3)

    def test_eC15(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("!@#")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("123!@#")
        time.sleep(3)
    
    def test_eC16(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(" ")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        time.sleep(3)

    def test_eC17(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("!@88662682")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("88663682!@")
        time.sleep(3)

    def test_eC18(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys(" ")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        time.sleep(3)


    def test_eC19(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99")
        time.sleep(3)
    
        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("Guru99@")
        time.sleep(3)

        self.driver.refresh()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("gurugmail.com")
        time.sleep(3)

    def test_eC20(self):        
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.profile()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.find_element(By.NAME, "sub").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(1)