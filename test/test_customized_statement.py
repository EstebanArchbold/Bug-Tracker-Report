"""
Filename: test_customized_statement.py

INFT 1207 - Sp/Su 2023 __ Group 6
Test cases 8: Mini Statements, FINAL PROJECT

Members(Sort by name in alphabet orders):
#   Jiaxing Chen (Gary)

Test cases: 
    Project Section...:
    09 --- Customoized Statement (CS#)

File purpose:
#   Test Cases through Selenium to a website.
Test Site: 
#   http://demo.guru99.com/V4/

Last Updated on: August 8, 2023
Created on: August 4, 2023


# Testing login: (usrID:mngr520629 Passwd:mEdUbEb)

"""

# Generated by Selenium IDE
from ssl import AlertDescription
import pytest
import time
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Global variables for different testing accounts:
global user_id, user_passwd,Account_No
user_id = "mngr520629"
user_passwd = "mEdUbEb"
AccountNo = "120937"

class Test_Section09():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

        # Pre-test config
        driver = self.driver

        # -3: Go to login webpage
        driver.get("https://demo.guru99.com/V4/")

        # -2: input User Credentials
        driver.find_element(By.NAME, "uid").send_keys(user_id)
        driver.find_element(By.NAME, "password").send_keys(user_passwd)

        # -1: Login
        driver.find_element(By.NAME, "btnLogin").click()

        # Step 0: Verify Login
        assert driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[3]/td").text == "Manger Id : " + user_id
        print("\nLogin Confirmed: Mainpage")
        
        print("Commence Test 09: Customized Statement")


    def teardown_method(self, method):
        self.driver.quit()



    # Test 09: Customized Statement
    # This segment of test codes test through the 'Customized Statement' tab of the website.

    # CS1-5: Verify account number
    def test9_CS1(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()

        # CS1: Account number cannot be empty
        print("Verify account number")
        driver.find_element(By.NAME, "accountno").send_keys("")
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        assert driver.find_element(By.ID, "message2").text == "Account Number must not be blank"
        print("CS1 Passed")

      
    def test9_CS2(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        
        # CS2: Account number must be numeric.
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("1234")
        assert driver.find_element(By.ID, "message2").text == ""
        print("CS2-1 Passed")
                
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        assert driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        print("CS2-2 Passed")


    def test9_CS3(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        
        # CS3: Account number cannot have special character.
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        assert driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        print("CS3-1 Passed")
        
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("!@#")
        assert driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        print("CS3-2 Passed")


    def test9_CS4(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS4: Account number cannot have blank space.
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123 12")
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)

        msg2 = driver.find_element(By.ID, "message2").text
        assert msg2 == "Characters are not allowed"
        if msg2 != "":
            print('CS4 Output: ', msg2)


    def test9_CS5(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()

        # CS5: First Character cannot be space.
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(" ")
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)

        msg2 = driver.find_element(By.ID, "message2").text
        assert msg2 == "First character cannot have space"
        if msg2 != "":
            print('CS5 Output: ', msg2)

    def test9_CS6(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # Verify from Date field
        # CS6: click on the date field.
        driver.find_element(By.NAME, "fdate").click()
        assert driver.find_element(By.ID, "message26").text == "From Date Field must not be blank"
        print("CS6 Passed")

    def test9_CS7(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # Verify from Date field
        # CS7: click on the date field
        driver.find_element(By.NAME, "tdate").click()
        assert driver.find_element(By.ID, "message27").text == "From Date Field must not be blank"
        print("CS7 Passed")

    #CS8-11 Number of Transaction
    print("Verify Minimum Transaction Value")
    def test9_CS8(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS8: Minimum Transaction Value must be numeric
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("1234")
        msg12 = driver.find_element(By.ID, "message12").text
        assert msg12 == ""
        print("\nCS8-1 Passed: ", msg12)
        
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("Acc123")
        msg12 = driver.find_element(By.ID, "message12").text
        assert msg12 == "Characters are not allowed"
        print("CS8-2 Passed: ", msg12)

    def test9_CS9(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        #CS9: Minimum Transaction Value cannot have special character
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("123!@#")
        msg12 = driver.find_element(By.ID, "message12").text

        assert msg12 == "Special characters are not allowed"
        print("\nCS9-1 Passed: ", msg12)
        
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("!@#")
        msg12 = driver.find_element(By.ID, "message12").text
        assert msg12 == "Special characters are not allowed"
        print("CS9-2 Passed: ", msg12)

    def test9_CS10(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS10: Minimum Transaction Value cannot have blank space
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("123 12")
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)
        
        msg12 = driver.find_element(By.ID, "message12").text
        assert msg12 == "Characters are not allowed"
        if msg12 != "Characters are not allowed":
            print('=CS10 Output inconsistent! :', msg12)

    def test9_CS11(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS11: First Character cannot be space
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(" ")
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)

        msg12 = driver.find_element(By.ID, "message12").text
        assert msg12 == "First character cannot have space"
        if msg12 != "First character cannot have space":
            print('=CS11 Output inconsistent! :', msg12)

    #CS12-15: Verify Number Transaction Value
    print("Verify Number of Transaction")
    def test9_CS12(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS12: Minimum Transaction Value must be numeric
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("1234")
        msg13 = driver.find_element(By.ID, "message13").text
        assert msg13 == ""
        print("CS12-1 Passed")
        
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("Acc123")
        msg13 = driver.find_element(By.ID, "message13").text
        assert msg13 == "Characters are not allowed"
        print("CS12-2 Passed")

    def test9_CS13(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS13: Number of transaction have special character
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("123!@#")

        msg13 = driver.find_element(By.ID, "message13").text
        assert msg13 == "Number of Transaction cannot have special character"
        if msg13 != "Number of Transaction cannot have special character":
            print('=CS13-1:', msg13)

        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("!@#")
        msg13 = driver.find_element(By.ID, "message13").text
        assert msg13 == "Number of Transaction cannot have special character"
        if msg13 != "Number of Transaction cannot have special character":
            print('CS13-2:', msg13)

    def test9_CS14(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS14: Number of transaction cannot have blank space
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("123 12")
        driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)

        msg13 = driver.find_element(By.ID, "message13").text
        assert msg13 == "Characters are not allowed"
        if msg13 != "Characters are not allowed":
            print('=CS14 Output inconsistent! :', msg13)

    def test9_CS15(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # CS15: First Character cannot be space
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys(" ")
        driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)

        msg13 = driver.find_element(By.ID, "message13").text
        assert msg13 == "First character cannot have space"
        if msg13 != "First character cannot have space":
            print('=CS15 Output inconsistent! :', msg13)

    def test9_CS16(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # Verify Buttons
        alert = Alert(driver)
        ## AccountNo = "120937"
        # this variable has delcared ahead. If the program cannot find it uncomment the above line.
        FromDate = "01092023"
        ToDate = "04142023"
        AmountMin = "4070"
        NumOfTrans = "1"
        
        # CS16: Reset Button
        print("CS16: Input testing AccountNo: ", AccountNo)

        driver.find_element(By.NAME, "accountno").send_keys(AccountNo)
        driver.find_element(By.NAME, "fdate").send_keys(FromDate)
        driver.find_element(By.NAME, "tdate").send_keys(ToDate)
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(AmountMin)
        driver.find_element(By.NAME, "numtransaction").send_keys(NumOfTrans)
        sleep(1)
        driver.find_element(By.NAME, "res").click()
        sleep(1)
        driver.find_element(By.NAME, "AccSubmit").click()
        sleep(3)
        assert driver.title == "Please fill all fields"
        print("CS16:", alert.text)
        alert.accept()

    def test9_CS17(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()

        # Verify Buttons
        alert = Alert(driver)
        ## AccountNo = "120937"
        # this variable has delcared ahead. If the program cannot find it uncomment the above line.
        FromDate = "01092023"
        ToDate = "04142023"
        AmountMin = "4070"
        NumOfTrans = "1"

        # CS17: Make a valid attempt
        print("CS17: Input testing AccountNo: ", AccountNo)
        alert = Alert(driver)
        driver.find_element(By.NAME, "accountno").send_keys(AccountNo)
        driver.find_element(By.NAME, "fdate").send_keys(FromDate)
        driver.find_element(By.NAME, "tdate").send_keys(ToDate)
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(AmountMin)
        driver.find_element(By.NAME, "numtransaction").send_keys(NumOfTrans)
        sleep(1)
        driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        assert driver.title == "Guru99 Bank Customised Statement Page"
        sleep(3)
        print("CS17 Passed")
        driver.back()
        
