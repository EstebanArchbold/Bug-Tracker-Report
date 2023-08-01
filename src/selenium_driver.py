from selenium import webdriver

class SeleniumDriver:
    def __init__(self, browser="chrome"):
        # Initialize the WebDriver based on the chosen browser
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser. Only 'chrome' and 'firefox' are supported.")

    def open_url(self, url):
        # Open a URL in the browser
        self.driver.get(url)

    def find_element_by_id(self, element_id):
        # Find and return an element by its ID
        return self.driver.find_element_by_id(element_id)

    def find_element_by_xpath(self, xpath):
        # Find and return an element by its XPath
        return self.driver.find_element_by_xpath(xpath)

    def click_element(self, element):
        # Click on an element
        element.click()

    def close(self):
        # Close the browser
        self.driver.quit()

