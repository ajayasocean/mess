# Auto-suggestive dynamic dropdowns
from Selenium.CallDriver import CallDriver
import time


def dynamic_dropdown(browser):
    url = "https://rahulshettyacademy.com/AutomationPractice"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.implicitly_wait(5)
    print(driver.title)

    # finding autosuggestive dynamic dropdown and its with via common locator
    auto_dropdown = driver.find_element_by_id("autocomplete")
    auto_dropdown.send_keys("ind")

    # now using css locator to find elements from dropdpwn
    res_countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] div")
    print(len(res_countries))
    for country in res_countries:
        if country.text == 'India':
            print(country.text)
            country.click()
            break
    # applying assertion
    assert driver.find_element_by_id("autocomplete").get_attribute('value') == 'India'
    driver.close()
    driver.quit()
    print("DynamicDropDown finished execution")
