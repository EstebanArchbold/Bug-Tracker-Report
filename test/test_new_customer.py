import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestNewCustomerCreation(unittest.TestCase):
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
        

    def test_VerifyNameField_NC1(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC1.png")


    def test_VerifyNameField_NC2(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("1234")
        self.driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC2.png")
        self.driver.find_element(By.NAME, "name").clear()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("name123")
        self.sleep_and_screenshot("test_eC2a.png")

    def test_VerifyNameField_NC3(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("name!@#")
        self.sleep_and_screenshot("test_eC3.png")
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").clear()
        self.driver.find_element(By.NAME, "name").send_keys("!@#")
        self.sleep_and_screenshot("test_eC3a.png")
    
    def test_VerifyNameField_NC4(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys(" name")
        self.driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC4.png")

    def test_VerifyAdressField_NC5(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC5.png")
    
    def test_VerifyAdressField_NC6(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys(" 1234")
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC5.png")
    
    def test_VerifyCityField_NC7(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC7.png")

    def test_VerifyCityField_NC8(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("1234")
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC8.png")
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city123")
        self.sleep_and_screenshot("test_eC8a.png")

    def test_VerifyCityField_NC9(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city!@#")
        self.sleep_and_screenshot("test_eC9.png")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "city").send_keys("!@#")
        self.sleep_and_screenshot("test_eC9a.png")
    
    def test_VerifyCityField_NC10(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys(" city")
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC10.png")

    def test_VerifyStateField_NC11(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC11.png")
    
    def test_VerifyStateField_NC12(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("1234")
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC12.png")
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("state1234")
        self.sleep_and_screenshot("test_eC12a.png")

    def test_VerifyStateField_NC13(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("State!@#")
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC13.png")
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("!@#")
        self.sleep_and_screenshot("test_eC13a.png")

    def test_VerifyStateField_NC14(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(" state")
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC14.png")

    def test_VerifyPINField_NC15(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234")
        self.sleep_and_screenshot("test_eC15.png")
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("PIN1234")
        self.sleep_and_screenshot("test_eC15a.png")
    
    def test_VerifyPINField_NC16(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC16.png")

    def test_VerifyPINField_NC17(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234567")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC17.png")
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234")
        self.sleep_and_screenshot("test_eC17a.png")
    
    def test_VerifyPINField_NC18(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("!@#")
        self.sleep_and_screenshot("test_eC18.png")
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("123!@#")
        self.sleep_and_screenshot("test_eC18a.png")
    
    def test_VerifyPINField_NC19(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys(" 1234")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC19.png")
    
    def test_VerifyPINField_NC20(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("12 34 ")
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC20.png")

    def test_VerifyMobileNumberField_NC21(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC21.png")

    def test_VerifyMobileNumberField_NC22(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(" 1234")
        self.sleep_and_screenshot("test_eC22.png")
        
    def test_VerifyMobileNumberField_NC23(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("123 123")
        self.sleep_and_screenshot("test_eC23.png")
    
    def test_VerifyMobileNumberField_NC24(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC24.png")
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("!@88662682")
        self.sleep_and_screenshot("test_eC24a.png")
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("!@88663682!@")
        self.sleep_and_screenshot("test_eC24b.png")

    def test_VerifyMobileEmailField_NC25(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC25.png")

    def test_VerifyMobileEmailField_NC26(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail ")
        self.sleep_and_screenshot("test_eC26.png")
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99")
        self.sleep_and_screenshot("test_eC26a.png")
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("Guru99@")
        self.sleep_and_screenshot("test_eC26b.png")
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail.")
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").click()
        self.sleep_and_screenshot("test_eC26c.png")
        self.driver.find_element(By.NAME, "emailid").clear()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail.com")
        self.sleep_and_screenshot("test_eC26c.png")

    def test_VerifyMobileEmailField_NC27(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys(" guru99@gmail.com")
        self.sleep_and_screenshot("test_eC27.png")

    def test_VerifyPasswordField_NC28(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys(Keys.TAB)
        self.sleep_and_screenshot("test_eC28.png")


    def sleep_and_screenshot(self, screenshot_name):
        time.sleep(3)  # Pause for 2 seconds
        self.driver.save_screenshot(screenshot_name)


if __name__ == "__main__":
    unittest.main()
