# Handling Java/JavaScript Alert pop-ups using selenium
from Selenium.CallDriver import CallDriver
import time


def alerts_script(browser):
    url = "https://rahulshettyacademy.com/AutomationPractice"
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.implicitly_wait(5)
    print(driver.title)

    # single option alert
    driver.find_element_by_xpath("//input[@name='enter-name']").send_keys('Test')
    driver.find_element_by_id('alertbtn').click()

    # DeprecationWarning: use driver.switch_to.alert instead alert = driver.switch_to_alert()
    alert = driver.switch_to.alert
    print(alert.text)
    assert 'Test' in alert.text

    # accepting the alert to close it
    alert.accept()

    # 2 option alert (cancelling an alert)
    driver.find_element_by_xpath("//input[@name='enter-name']").send_keys('Test')
    driver.find_element_by_id('confirmbtn').click()

    # DeprecationWarning: use driver.switch_to.alert instead alert = driver.switch_to_alert()
    alert_bi = driver.switch_to.alert
    print(alert_bi.text)

    # cancelling the alert to close it
    alert.dismiss()
    driver.close()
    driver.quit()
    print("alerts.py finished execution")
