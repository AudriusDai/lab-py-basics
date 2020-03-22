readMe1 = open('exampleFile.txt', 'r')
text = readMe1.read()  # cannot reuse readMe1 for readlines :////
readMe2 = open('exampleFile.txt', 'r')
lines = readMe2.readlines()

print(text)
print(lines)
