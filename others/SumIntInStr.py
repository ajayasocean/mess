
str = "10sdffsfd90sdf40df100"

temp = '0'
total = 0

for i in str:
    if i.isdigit():
        temp += i

    else:
        total += int(temp)
        temp = '0'
print('final', total+int(temp))
