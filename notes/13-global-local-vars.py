x = 6


def example():
    z = 5
    print(z)


# trows local variable issue...
'''
def example2():
    print(x)
    print(x+5)
    x += 2
'''


def example3():
    global x
    print(x)
    print(x+5)
    x += 2


def example4():
    localx = x
    print(localx)
    print(localx+5)
    localx += 2
    return localx


# example()
# example2()
# example4()

print(x)
x = example4()
print(x)
