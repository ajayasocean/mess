# invoking required browser type
from Selenium.driver import Driver


class CallDriver(Driver):
    type = None

    # calling Driver calls to launch selected browser
    def call_driver(self, driver_type):
        self.type = driver_type
        if self.type == "headless_chrome":
            return Driver.call_headless_chrome(self)
        elif self.type == "chrome":
            return Driver.call_chrome(self)
        elif self.type == "firefox":
            return Driver.call_firefox(self)
        else:
            return None
