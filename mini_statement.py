"""
Filename: mini_statement.py
Purpose: Test case for testing: Inquire a mini statement

Last Updated on: August 4, 2023
Created on: August 4, 2023


"""

from selenium_driver import SeleniumDriver

def test_mini_statement():
    driver = SeleniumDriver()
    driver.open_url("http://www.demo.guru99.com/V4/")

    # Your test case logic here

    driver.close()