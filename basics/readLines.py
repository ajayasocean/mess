# readlines() This method returns all lines from files as output in list form.
file1 = open('/Backend/config/testTextFile.txt')
lines = file1.readlines()
for line1 in lines:
    print(line1)
file1.close()
