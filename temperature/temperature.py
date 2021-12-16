try:
    def from_kelvin(*settings):
        if 'celsius' in settings:
            t = settings[0] - 273
            return t
        elif 'fahrenheit' in settings:
            t = settings[0] - 273
            f = 1.8 * t + 32
            return f


    def from_fahrenheit(*settings):
        if 'kelvin' in settings:
            t = (settings[0] - 32) / 1.8
            T = t + 273
            return T
        elif 'celsius' in settings:
            t = (settings[0] - 32) / 1.8
            return t


    def from_celsius(*settings):
        if 'kelvin' in settings:
            T = settings[0] + 273
            return T
        elif 'fahrenheit' in settings:
            f = settings[0] * 1.8 + 32
            return f

except:
    print(f'Есть обязательное правило введения: Sys измерения температуры, известная вам (Число, "'
          f'Необходимая_sys_измерения_температуры"). Пример: celsius(13,\'kelvin\')')
    print(f'Доступные: fahrenheit(Фаренгейт), celsius(градус Цельсии), kelvin(Кельвин)')



''' 
DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY
you can find examples in file.py 
created by Kamol Khursandov in 2021
DIVFAY DIVFAY DIVFAY DIVFAY DIVFAY
'''
