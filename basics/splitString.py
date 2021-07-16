# split functions

str1 = "07-09-2020"

print(str1.split("-", 1))

print(str1.split("-"))

list1 = str1.split("-")
print(list1[2])

name = "Ajay Sagar"
splitted_name = name.split()
print(splitted_name)
print(type(splitted_name))
print(str1.rsplit("-", 1))
