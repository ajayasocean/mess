# writing a program to print output rad from file using readline() method.
file1 = open('/Backend/config/testTextFile.txt')
line1 = file1.readline()
i = 0
while line1 != '':
    i += 1
    print(i, '.', line1)
    line1 = file1.readline()
file1.close()
