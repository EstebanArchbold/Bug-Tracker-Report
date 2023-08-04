"""
Filename: new_account_test.py
Purpose: Test case for testing: Add new account.

Last Updated on: August 4, 2023
Created on: August 4, 2023


"""

from selenium_driver import SeleniumDriver

def test_new_account():
    driver = SeleniumDriver()
    driver.open_url("http://www.demo.guru99.com/V4/")

    # Your test case logic here

    driver.close()
