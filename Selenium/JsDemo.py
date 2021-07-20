# Java Script HTML DOM document.
from Selenium.CallDriver import CallDriver


def js_demo(browser):
    url = "https://rahulshettyacademy.com/angularpractice"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    # driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)

    # entering text into name field
    driver.find_element_by_name("name").send_keys('Test')

    # trying to fetch entered text into name field using .text method.
    print(driver.find_element_by_name("name").text)

    # fetch entered text into name field using get_attribute method of selenium
    print(driver.find_element_by_name("name").get_attribute('value'))

    # fetch entered text into name field using pure java script dom
    print(driver.execute_script('return document.getElementsByName("name")[0].value'))

    # clicking on a button on web page using execute_script.
    shp_btn = driver.find_element_by_css_selector("a[href*='shop']")
    driver.execute_script("arguments[0].click();", shp_btn)

    # scrolling down on web page using java script as selenium don't have scroll method
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    driver.close()
    driver.quit()
    print("JsDemo.py finished execution")
