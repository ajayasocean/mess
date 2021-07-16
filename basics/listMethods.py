# append() method

avg = ['Steve', 'Tony']

print('Appended elements(values) in the list\n', avg)

# extend menthod

avg2 = ['Banner', 'Thor']
avg.extend(avg2)
print(avg)
print(avg2)

# extend via a string
list1 = ['a', 'e', 'i']
vow = "ou"
list1.extend(vow)
print("Vowels are ", list1)

# extend via a tuple.

team = ('Romanoff', 'clint')
avg.extend(team)
print('after extending by a tuple', avg)

# appending a list using another list as argument
vowels = ['a', 'e', 'i']
vo = ['o', 'u']
vowels.append(vo)
print(vowels)

# count() method

list1 = ["a", "c", "b", "c", "a", "h", "l", 1, 2, 3, 4]
print(list1.count("a"))
print(list1.count("h"))
print(list1.count('o'))

# index()

os = ['kali', 'Ubuntu', 'debian', 'RHEL', 'Centos']
print(os.index('debian'))
os.append('kali')
print(os)
print(os.index('kali'))

# insert()

avgr = ['Tony', 'Banner', 'Thor']
avgr.insert(0, 'Steve')
print(avgr)
avgr.insert(4, 'Natasha')
print(avgr)

# remove ()
av = ['Tony', 'Steve', 'Loki', 'Thor']
av.remove("Loki")
print(av)
# av.remove('cap') for testing value error

num = [1, 2, 3, 4, 5, 6, 4, 1, 7]
num.remove(1)
print(num)

# pop ()
got = ["Tyrion", "Sansa", "Arya", "Joffrey", "Ned-Stark"]

print(got.pop())
print(got.pop())
print(got)
print(got.pop(0))
print(got)


# sort ()
list1 = [5, 6, 7, 1, 4, 2, 0, 4, 2, 8]
list1.sort()
print("Sorted list1", list1)
list2 = [5, 6, 7, 1, 4, 2, 0, 4, 2, 8]
list2.sort(reverse=True)
print("Sorted list2", list2)

avn = ['hulk', 'iron-man', 'Captain-America', 'Thor', 'vision', 'Clint']
avn.reverse()
print(avn)
