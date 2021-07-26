import math


def find_maximum_height(n):

    # calculating portion inside the square root
    portion = 1 + 8*n
    max_h = (-1 + math.sqrt(portion)) / 2
    return int(max_h)


# Driver code to test above method
n = 10
print(find_maximum_height(n))

