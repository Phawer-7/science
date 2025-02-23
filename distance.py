import numpy as np
import math 

x = np.array((1,2,3))
y = np.array((5,4,6))

def distance_between_dots(x, y):
    if x.ndim == y.ndim:
        r = (x - y)**2
        return math.sqrt(sum(r))
    else:
        return None
    

print(distance_between_dots(x, y))
