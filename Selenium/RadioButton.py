# finding and clicking radio buttons.
from Selenium.CallDriver import CallDriver
import time


def radio_button(browser):
    url = "https://rahulshettyacademy.com/AutomationPractice"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    print(driver.title)

    # finding radiobutton via common locator
    radio_buttons = driver.find_elements_by_name('radioButton')
    print(len(radio_buttons))
    radio_buttons[2].click()
    assert radio_buttons[2].is_selected()
    driver.close()
    driver.quit()
    print("RadioButton.py finished execution")
