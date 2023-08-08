# new_customer_test.py
from selenium_driver import SeleniumDriver

def test_new_customer_creation():
    driver = SeleniumDriver()
    driver.open_url("http://www.demo.guru99.com/V4/")

    # Your test case logic here

    driver.close()
