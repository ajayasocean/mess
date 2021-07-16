# Use the list, [1,2,4,5,1,1,4,1,56], and find the index of all the 1 elements.

inputList = [1, 2, 4, 5, 1, 1, 4, 1, 56]
length = len(inputList)
list2 = []
for i in range(length):
    if inputList[i] == 1:
        list2.append(i)
print(list2)

# Exercise 4: above task by comprehension
print([i for i in range(length) if inputList[i] == 1])
