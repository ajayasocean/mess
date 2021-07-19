""" Handle child windows/tabs in selenium
    https://the-internet.herokuapp.com

"""
from Selenium.CallDriver import CallDriver


def switch_child(browser):
    url = "https://the-internet.herokuapp.com/windows"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)

    # clicking on link text
    driver.find_element_by_link_text("Click Here").click()

    # finding window id for pages opened by selenium
    child_window = driver.window_handles[1]

    # switching selenium to child window
    driver.switch_to_window(child_window)
    print(driver.title)

    # getting text from child Window
    # print(driver.find_element_by_xpath("//div[@class='example']/h3").text)
    assert "New Window" == driver.find_element_by_tag_name("h3").text

    # closing child window
    driver.close()

    # finding window id for pages opened by selenium
    parent_window = driver.window_handles[0]

    # switching back to parent window
    driver.switch_to_window(parent_window)
    print(driver.title)

    driver.close()
    driver.quit()
    print("ChildWindow.py finished Execution")

