# initiating web driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    logger = ["--verbose", "--log-path=/Users/ajaysagar/ocean/mess/Selenium/chromedriver.log"]  # log file for chrome driver

    def call_chrome(self):
        # to run run script in chromedriver
        w_driver = webdriver.Chrome('/usr/local/share/chromedriver', service_args=self.logger)
        return w_driver

    def call_headless_chrome(self):
        # to run chromedriver in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        w_driver = webdriver.Chrome('/usr/local/share/chromedriver', service_args=self.logger, options=chrome_options)
        return w_driver

    def call_firefox(self):
        # to run run script in firefox
        w_driver = webdriver.Firefox()
        return w_driver
