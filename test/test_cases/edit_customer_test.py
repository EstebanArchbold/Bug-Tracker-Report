# edit_customer_test.py
from selenium_driver import SeleniumDriver

def test_edit_customer():
    driver = SeleniumDriver()
    driver.open_url("http://www.demo.guru99.com/V4/")

    # Your test case logic here

    driver.close()