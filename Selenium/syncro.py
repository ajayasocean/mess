"""# Synchronization (Implicit & Explicit) waits in selenium
# https://rahulshettyacademy.com/seleniumPractise
# promocode: rahulshettyacademy
"""
from Selenium.CallDriver import CallDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def cart_script(browser):
    url = "https://rahulshettyacademy.com/seleniumPractise"
    added_products = []  # initiating empty list for products that will be added to cart
    in_cart_items = []  # initiating empty list for products in cart
    drive_obj = CallDriver()
    driver = drive_obj.call_driver(browser)
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    driver.implicitly_wait(5)
    print(driver.title)

    # finding all products and storing their names in a list
    product_list = driver.find_elements_by_xpath("//button[text()='ADD TO CART']/parent::div/parent::div/h4")
    product_names = []
    for product in product_list:
        product_names.append(product.text)
    print(product_names)

    # entering search test in search bar
    driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys('ber')
    time.sleep(3)
    # validating product count after entering ber in search box
    product_count = len(driver.find_elements_by_xpath("//div[@class='product']"))
    print("Product count = ", product_count)

    # counting visible add to cart buttons
    add_to_cart = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
    print('Buttons count = ', len(add_to_cart))

    # //button[text()='ADD TO CART']/parent::div/parent::div/h4 using this locator to validate product names
    for button in add_to_cart:
        # grabbing product names and adding to the list to compare on next page.
        added_products.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)

        # clicking on all the Add to cart button
        button.click()
    print(added_products)

    # validating search functionality is working fine.
    # asserting added_products list is in product_names
    for each in added_products:
        assert each in product_names

    # clicking the cart icon xpath: img[alt='Cart']
    driver.find_element_by_css_selector("img[alt = 'Cart']").click()

    # clicking on proceed to checkout
    driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
    time.sleep(5)

    # explicit wait
    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))

    # finding product names in cart and storing in list to compare
    cart = driver.find_elements_by_xpath("//p[@class='product-name']")

    # adding product names to list
    for items in cart:
        in_cart_items.append(items.text)
    print(in_cart_items)

    # validating items in cart are same as added from listing page.
    assert added_products == in_cart_items

    # verifying if sum of product amount on checkout matches with total amount
    product_amounts = driver.find_elements_by_xpath("//tr/td[5]/p")

    product_total = 0
    for p_amt in product_amounts:
        product_total = product_total + float(p_amt.text)
    print("Product amount total = ", product_total)

    # entering data into promo code field
    driver.find_element_by_xpath("//input[@class='promoCode']").send_keys('rahulshettyacademy')
    print(driver.current_url)

    # grabbing Amount before discount is applied.
    actual_amount = float(driver.find_element_by_xpath("//span[@class='totAmt']").text)
    print("Total Amount", actual_amount)

    # validating total amount matches sum of product amounts.
    assert product_total == actual_amount

    # clicking Apply button
    driver.find_element_by_xpath("//button[@class='promoBtn']").click()

    # checking for code applied text.
    assert 'applied' in driver.find_element_by_xpath("//span[@class='promoInfo']").text

    # grabbing discounted amount
    discounted_amount = float(driver.find_element_by_xpath("//span[@class='discountAmt']").text)

    # validating actual total amount is greater than discounted amount.
    assert discounted_amount < actual_amount

    driver.close()
    driver.quit()
    print("syncro.py finished Execution")
