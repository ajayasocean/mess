# write a program to find out second highest item from below tuple without sorting and using in-built functions.
tup = (123, 456, 112, 346, 678, 234)

# easier way using built-in functions
sort_tup = sorted(tup)
print(sort_tup)
tup_len = len(sort_tup)
print(tup_len)
print(sort_tup[tup_len-2])

# without using in-built functions
mx = max((tup[0], tup[1]))
smx = min((tup[0], tup[1]))
n = len(tup)
for i in range(2, n):
    if tup[i] > mx:
        smx = mx
        mx = tup[i]
    elif tup[i] > smx and tup[i] != mx:
        smx = tup[i]

print("Second highest number is : ", str(smx))
