from Vector import Vector
import math

def circular(x_0, y_0, x_scale, y_scale, time_scale=1, phase=0):
    def f(t):
        return Vector(x_0 + x_scale*math.cos(t*time_scale - 2*math.pi*phase),
                     y_0 + y_scale*math.sin(t*time_scale - 2*math.pi*phase))
    return f

def sin_n_impulses(x_0, y_0, n, y_scale, time_scale=1, phase=0):
    def f(t):
        #want 
        if n_box((t*time_scale - phase)/(2*math.pi),n) :
            return Vector(x_0, y_0 + y_scale*math.sin(t*time_scale - 2*math.pi*phase))
        else:
            return Vector(x_0, y_0)
    return f

def n_box(k, n):
    """Returns true if k in [2i, 2(i+1)], i = 0,...,n-1"""
    return (k < 2*n) and (int(k) % 2 == 0)