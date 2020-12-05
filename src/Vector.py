# Copyright Daniel Rastelli 2020

class Vector:
    """ A class for representing vectors in R2. """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, v2):
        """ Override addition. """
        x_new = self.x + v2.x
        y_new = self.y + v2.y

        return Vector(x_new, y_new)

    def __sub__(self, v2):
        x_new = self.x - v2.x
        y_new = self.y - v2.y
        
        return Vector(x_new, y_new)

    def scale(self, a):
        return Vector(a * self.x, a * self.y)

    def __eq__(self, v2):
        return (self.x == v2.x) and (self.y == v2.y)

    def to_tuple(self, round=False):
        if round:
            return (int(self.x), int(self.y))
        return (self.x, self.y)