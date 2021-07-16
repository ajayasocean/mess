# managing dropdowns on webpage
from selenium.webdriver.support.select import Select
from Selenium.CallDriver import CallDriver
import time


def dropdown(browser):
    url = "https://rahulshettyacademy.com/angularpractice"
    # calling CallDriver class to decide browser
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    driver.implicitly_wait(5)
    print(driver.title)
    dropdown1 = Select(driver.find_element_by_id("exampleFormControlSelect1"))
    # dropdown methods
    dropdown1.select_by_visible_text("Female")
    dropdown1.select_by_index(0)
    driver.close()
    driver.quit()
    print("DropdownDemo finished dropdown")
