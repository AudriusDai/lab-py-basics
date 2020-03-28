import sys

sys.stderr.write("This is the stderr \n")
sys.stdout.write("This is the stdout \n")


print(sys.argv)


def main(arg):
    print(arg)

# you can use this to invoke python methods out from command line by passing
# the arguments via argv and execute the function right away.
