"""
Filename: edit_account_test.py
Purpose: Test case for testing: Edit a account.

Last Updated on: August 4, 2023
Created on: August 4, 2023


"""

from selenium_driver import SeleniumDriver

def test_edit_account():
    driver = SeleniumDriver()
    driver.open_url("http://www.demo.guru99.com/V4/")

    # Your test case logic here

    driver.close()