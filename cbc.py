from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class ChromeBrowserController:

    def __init__(self, driver_path, headless=False):
        if headless:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--headless")
            self.driver = webdriver.Chrome(driver_path, options=self.options)
        else:
            self.driver = webdriver.Chrome(driver_path)

    # Uses the previous url to compare it to the current url
    # in order to verify the page has completely loaded.
    def wait_page_to_load(self, timeout, old_url):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))

    def select_elements_by_xpath(self, xpath):
        elements = self.driver.find_element_by_xpath(xpath)
        return Select(elements)
