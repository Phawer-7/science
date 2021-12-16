import temperature

x = temperature.from_celsius(24, 'kelvin')  # received 546
y = temperature.from_celsius(24, 'fahrenheit')  # received 64

if (z := temperature.from_fahrenheit(y, 'kelvin')) == x:
    print(f'{x} Kelvin equals {y} Fahrenheit')
else:
    print(f'{x}K doesn\'t equal {z}K({y} Fahrenheit)')
