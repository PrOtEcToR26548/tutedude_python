# Task 1

n=int(input('Enter a number: '))
def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
result = factorial(n)
print(f'factorial of {n} is {result}')

# Task 2

import math

n = int(input('Enter the number: '))

def math_func(n):
    print('Square root of number is : ',math.sqrt(n))
    print('Logarthm of number is : ',math.log(n))
    print('Sine of number is : ',math.sin(n))
math_func(n)