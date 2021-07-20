""" Handle child frame, frameset, iframe in selenium
    https://the-internet.herokuapp.com/

"""
from Selenium.CallDriver import CallDriver


def handle_frames(browser):
    url = "https://the-internet.herokuapp.com/iframe"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)

    # switching to iframes
    driver.switch_to_frame("mce_0_ifr")

    # clearing and entering content in textbox on iframe.
    driver.find_element_by_css_selector("#tinymce").clear()
    driver.find_element_by_css_selector("#tinymce").send_keys("In the iframe now")

    # switching back to main web page
    driver.switch_to_default_content()

    # fetching heading text from page
    print(driver.find_element_by_tag_name("h3").text)

    driver.close()
    driver.quit()
    print("FramesDemo.py finished Execution")
