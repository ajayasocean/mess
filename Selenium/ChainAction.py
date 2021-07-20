""" Handle advance interactions in selenium with ActionChain class
    https://rahulshettyacademy.com/AutomationPractice
    Mouse Hover, click

"""
from selenium.webdriver import ActionChains
from Selenium.CallDriver import CallDriver


def adv_interactions(browser):
    url = "https://rahulshettyacademy.com/AutomationPractice"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)

    # using Action chain class moving to "Mouse Hover" Button on page.
    action = ActionChains(driver)
    ms_btn = driver.find_element_by_id("mousehover")
    action.move_to_element(ms_btn).perform()

    # move to appeared menu from hover
    child_menu = driver.find_element_by_link_text("Reload")
    action.move_to_element(child_menu).click().perform()

    # is_displayed() method to check whether a particular element in displayed on webpage.
    assert driver.find_element_by_id("displayed-text").is_displayed()

    # clicking on hide button.
    driver.find_element_by_id("hide-textbox").click()

    # again checking for text box
    assert not driver.find_element_by_id("displayed-text").is_displayed()

    driver.close()
    driver.quit()
    print("ChainAction.py finished Execution")
