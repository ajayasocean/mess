print("Name", "Marks", "Age")
print("John Doe", 80.67, "27")
print("Bhaskar", 76.908, "27")
print("Mohit", 56.98, "25")
print("Name \tMarks \tAge")
print("%s \t%5.2f \t%5d" %("John Doe", 80.67, 27))
print("%s \t%5.2f \t%5d" %("Bhaskar", 76.901, 27))
print("%s \t%5.2f \t%5d" %("Mohit", 56.98, 25))

# .format()
print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))

# Formatted String Literal (f-String)
quantity = 6
item = 'bananas'
price = 1.74
print(f'{quantity} {item} cost ${price}')
