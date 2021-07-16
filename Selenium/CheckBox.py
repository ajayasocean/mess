# handling checkbox dynamically using selenium
from Selenium.CallDriver import CallDriver
import time


def checkbox(browser):
    url = "https://rahulshettyacademy.com/AutomationPractice"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.implicitly_wait(5)
    print(driver.title)

    # finding checkbox via common locator using xpath
    check_list = driver.find_elements_by_xpath("//input[@type='checkbox']")
    print(len(check_list))
    for check_box in check_list:
        print(check_box.get_attribute('value'))
        if check_box.get_attribute('value') == 'Option1':
            check_box.click()
            assert check_box.is_selected()
    driver.close()
    driver.quit()
    print("CheckBox.py finished execution")
