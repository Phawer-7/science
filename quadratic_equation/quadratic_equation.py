import math

# Solution of a quadratic equation

lang = None

lang_words = {
    'en': 'There are not roots, D is smaller than 0.',
    'ru': 'Нет корней, дискриминант(D) меньше 0',

    'en_error_msg': 'Mandatory rule: input with spaces!. Example: "+1 * x ** 2 +3 * x + 9= 0". ** is power',
    'ru_error_msg': 'Важное правило: должен быть пробел после каждого числа и оператора! '
                    'Пример: "+1 * x ** 2 +3 * x + 9= 0". где ** степень '
}


# main function declaration
def quadratic_equation(equation):
    try:
        equation = equation.split()
        a, b, c = int(equation[0]), int(equation[5]), int(equation[8])
    except ValueError:
        if lang is None or lang == 'en':
            return lang_words['en_error_msg']
        elif lang == 'ru':
            return lang_words['ru_error_msg']

    try:
        D = math.sqrt(pow(b, 2) - 4 * a * c)
        if D > 0:
            x1 = (-b + D) / (2 * a)
            x2 = (-b - D) / (2 * a)
            return [x1, x2]
        else:
            x = -b / (2 * a)
            return x
    except ValueError:
        if lang is None or lang == 'en':
            return lang_words['en']
        elif lang == 'ru':
            return lang_words['ru']


def return_D(a, b, c):
    return pow(b, 2) - 4 * a * c


def square_root_D(a, b, c):
    try:
        return math.sqrt(pow(b, 2) - 4 * a * c)
    except ValueError:
        if lang is None or lang == 'en':
            return lang_words['en']
        elif lang == 'ru':
            return lang_words['ru']


'''
DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY 

Created by Kamol Khursandov in 2021, december. Tashkent/Uzbekistan.
Examples and how it works showed in run_and_example_file.py 
Github: Phawer-7  Telegram: ojfbv

DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY 
'''