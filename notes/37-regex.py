'''
Indenrifiers:
\d  - any number
\D  - anything but a number
\s  - space 
\S  - anything but a space
\w  - any char
\W  - anything but a char
.   - any char for a newline
\b  - the whitespace around words
\.  - a period

Modifiers:
{1,3} we're expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of a string
^ mathing the beginning of a string
| either or. i.e. \d{1,3} | \d{4,6}
[] range of "variance" [1-5a-qA-Z]
{x} expecting "x" amount

White Spave chars:
\n  new line
\s  space
\t  tab
\e  escape
\f  form feed
\r  return

DON'T FORGET:
. + * ? [ ] $ ^ () {} | \
if you want to use them you need to escape them. How? 

'''

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1

print(ageDict)
