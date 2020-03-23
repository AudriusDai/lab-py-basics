# list is mutable
# tuple is not :)

t = 5, 6, 2, 6  # rarely used. generated and iterated through faster.
t = (5, 6, 2, 6)

l = [5, 6, 2, 6]


def exampleFunc():
    return 15, 6


x, y = exampleFunc()


x = (5, 6, 2, 6)
y = [5, 6, 2, 6]

print(x[1])  # tuples also has index
