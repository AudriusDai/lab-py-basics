def simple_addition(num1, num2=59):
    answer = num1 + num2
    print('num1 is ', num1)
    print('num2 is ', num2)
    print(answer)


def basic_windows(width, height, font='TNR',
                  bgc='w', scrollBar=True):
    print(width, height, font, bgc)


simple_addition(1, 5)
simple_addition(9)

basic_windows(500, 350, bgc='a')
