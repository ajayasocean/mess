# write a program to print a given string in reverse as output.
# The concept to be used here is slicing in backward order.

# taking input from user
given_string = input('Please enter string you want to reverse\n')


# reverseString = given_string[::-1]


# doing it with a function
def reverse(given_string):
    return given_string[::-1]


reverseString = reverse(given_string)
print('Reverse of your string is \n', reverseString)
