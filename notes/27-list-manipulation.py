x = [515, 4, 5, 651, 5, 7, 5615, 15, 1, 515, 1]

# append
print('before: ', x)
x.append(2)
print('after:  ', x)

# insert at the index
x.insert(2, 99)
print('after:  ', x)

# remove
x.remove(99)
print('after:  ', x)

# slicing
print('from 5 to 7: ', x[5:7])
print('last value: ', x[-1])

# Useful when operating with two lists, when trying to find the value
print('with value 7 the index is: ', x.index(7))

print('count of value: ', x.count(7))
print(x.count(7))

# sorting the same list
x.sort()
print(x)

# string values
y = ['Janet', 'Jop', 'Al']
y.sort()

print(y)
