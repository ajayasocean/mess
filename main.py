# this will call the scripts under Selenium directory
# from Selenium.IntroSelenium import intro_selenium
# from Selenium.locators import locators
# from Selenium.MoreLocators import more_locators
# from Selenium.DropdownDemo import dropdown
# from Selenium.DynamicDropDown import dynamic_dropdown
# from Selenium.CheckBox import checkbox
# from Selenium.RadioButton import radio_button
# from Selenium.alerts import alerts_script
# from Selenium.syncro import cart_script
# from ZomatoScraper.scraping import scraping
# from puzzle.ManualPuzzle import man_puz
# from Selenium.ChildWindow import switch_child
# from Selenium.FramesDemo import handle_frames
# from Selenium.ChainAction import adv_interactions
# from Selenium.ActionClick import d_click
from Selenium.JsDemo import js_demo


def main():
    print("My mess, my hell")
    # passing browser type
    # browser = "chrome"
    browser = "headless_chrome"

    # calling IntroSelenium Script
    # intro_selenium(browser)

    # calling locators.py
    # locators(browser)

    # calling MoreLocators.py
    # more_locators(browser)

    # calling DropdownDemo.py
    # dropdown(browser)

    # calling DynamicDropDown.py
    # dynamic_dropdown(browser)

    # calling CheckBox.py
    # checkbox(browser)

    # calling RadioButton.py
    # radio_button(browser)

    # calling alerts.py
    # alerts_script(browser)

    # calling syncro.py
    # cart_script(browser)

    # calling ZomatoSraper project (scraping.py)
    # scraping()

    # calling chinese puzzle manual version
    # man_puz()

    # calling ChildWindow.py
    # switch_child(browser)

    # calling FramesDemo.py
    # handle_frames(browser)

    # calling ChainAction.py
    # adv_interactions(browser)

    # calling ActionClick.py
    # d_click(browser)

    # calling JsDemo.py
    js_demo(browser)


if __name__ == '__main__':
    main()
