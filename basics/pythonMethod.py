# user defined
import math


class Vehicle:
    def __init__(self, color):
        self.color = color

    def start(self):
        print("Starting engine")

    def showcolor(self):
        print(f"I am {self.color}")  # formated string literal


car = Vehicle('black')
car.start()
car.showcolor()

# another example
surName = input('Please enter your last Name:\n')


# print(surName)
class Test:
    def __init__(self, user):
        self.user = user

    def show_name(self):
        print(f'I am {self.user}')  # formatted string literal


testRef = Test(surName)
testRef.show_name()

# build in method
ceilVal = math.ceil(15.25)
print("Ceiling value of 15.25 is : ", ceilVal)
