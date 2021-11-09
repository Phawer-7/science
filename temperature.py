# x means 'don't know'

def fahrenheit(t, T):
    if t != 'x':
        f = t * 1, 8 + 32
    elif T != 'x':
        f = (T - 273) * 1, 8 + 32
    return f


def kelvin(t, f):
    if t != 'x':
        T = t + 273
    elif f != 'x':
        T = f + 273
    return T


def celsius(T, f):
    if T != 'x':
        t = T - 273
    elif f != 'x':
        t = (f - 32) / 1.8
    return t