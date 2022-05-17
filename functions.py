def add_np():
    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))

    print(num1, '+', num2, '=', num1 + num2)


def sub_p(num1, num2):
    print(num1, '-', num2, '=', num1 - num2)

def add_r(num1, num2):
    return num1 + num2

def add_nr(num1, num2):
    print(num1, '+', num2, '=', num1 + num2)


a = int(input('Enter first number'))
b = int(input('Enter second number'))

if add_r(a, b) > 100:
    print('Sum is greater than 100')

