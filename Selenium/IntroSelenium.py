from Selenium.CallDriver import CallDriver


def intro_selenium(browser):
    url1 = "https://imdb.com"
    url2 = "https://netflix.com"
    # browser = "headless_chrome"
    # calling CallDriver class to decide browser
    drive_obj = CallDriver()
    drive = drive_obj.call_driver(browser)
    drive.maximize_window()
    drive.get(url1)
    drive.implicitly_wait(5)
    print(drive.title)
    print(drive.current_url)
    drive.get(url2)  # navigating to new url
    drive.back()
    drive.refresh()
    drive.minimize_window()
    drive.close()
    drive.quit()
    print("Execution finished for intro_selenium")
