import math


# Solution of a quadratic equation

# main function declaration
def result(a, b, c):
    D = b ** 2 - 4 * a * c
    print(f'D equals: {D}')
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f'Roots are: {x1}, {x2}')
    elif D == 0:
        x = -b / (2 * a)
        print(f'single root {x}')
    else:
        print(f'These are not roots, D is smaller than 0.')


# Example:: user inputted: 5x**2+7x+3=0
# Mandatory rule: input with spaces!!!. Example: "+2 * x ** 2 +9 * x +3 = 0". ** is degree
equation = input('input your quadratic equation: ')
equation = equation.split()

a, b, c = int(equation[0]), int(equation[5]), int(equation[8])
result(a, b, c)

# https://github.com/Phawer-7/science/blob/main/quadratic_equation/quadratic_equation.py
