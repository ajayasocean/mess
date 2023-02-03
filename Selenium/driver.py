# initiating web driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    logger = ["--verbose", "--log-path=/Users/ajaysagar/ocean/mess/Selenium/chromedriver.log"]  # log file for chrome driver

    def call_chrome(self):
        # to run script in chromedriver
        w_driver = webdriver.Chrome('/usr/local/share/chromedriver', service_args=self.logger)
        # w_driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver.exe', service_args=self.logger)
        return w_driver

    def call_headless_chrome(self):
        # to run chromedriver in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--start-maximized")  # maximized mode
        # chrome_options.add_argument("--ignore-certificate-errors")  # ignoring certificate errors
        w_driver = webdriver.Chrome('/usr/local/share/chromedriver', service_args=self.logger, options=chrome_options)
        return w_driver

    def call_firefox(self):
        # to run script in firefox
        w_driver = webdriver.Firefox()
        return w_driver
