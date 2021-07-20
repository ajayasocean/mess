""" Handle advance interactions in selenium with ActionChain class
    double click, context click etc
    https://chercher.tech/practice/practice-pop-ups-selenium-webdriver

"""
from selenium.webdriver import ActionChains
from Selenium.CallDriver import CallDriver


def d_click(browser):
    url = "https://chercher.tech/practice/practice-pop-ups-selenium-webdriver"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)

    # using Action chain class for double click.
    action = ActionChains(driver)

    # right click using context click option.
    action.context_click(driver.find_element_by_id("double-click")).perform()

    # double clicking on button.
    action.double_click(driver.find_element_by_id("double-click")).perform()

    # switching to alert raised by double click
    alert = driver.switch_to_alert()
    print(alert.text)
    alert.accept()

    driver.close()
    driver.quit()
    print("ActionClick.py finished Execution")
