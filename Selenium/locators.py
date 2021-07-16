import time

from Selenium.CallDriver import CallDriver


def locators(browser):
    url1 = "https://rahulshettyacademy.com/angularpractice"
    # browser = "headless_chrome"
    # calling CallDriver class to decide browser
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url1)
    time.sleep(3)
    driver.implicitly_wait(5)
    driver.find_element_by_name('name')
    driver.close()
    driver.quit()
    print("locators.py Execution done")
