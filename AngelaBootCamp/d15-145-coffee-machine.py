# AngelaBootCamp/coffee.py
from AngelaBootCamp.coffee import SPECS
import json


def get_input():
    user_choice = input("What would you like? (espresso/latte/cappuccino): \n")
    if user_choice in SPECS.drinks:
        pass
        get_input()
    elif user_choice != "off":
        exit()
    elif user_choice == 'report':
        report = json.dumps(SPECS.resource, indent=2, ensure_ascii=False)
        print(report)
        get_input()
    else:
        print("Enter valid input")
        get_input()
    return


def main():
    # print(SPECS.resource)
    # print(SPECS.menu)
    user_choice = input("What would you like? (espresso/latte/cappuccino): \n")
    while user_choice != 'off':
        get_input()
    if user_choice != "off":
        exit()



if __name__ == '__main__':
    main()