﻿class Fraction(object):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()
    def __str__(self):
        return '%d/%d' % (self.__num, self.__den)
    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g
    def __neg__(self):  
        return '-%d/%d' % (self.__num, self.__den)
    def __invert__(self):  
        return '%d/%d' % (self.__den, self.__num)
    def __pow__(self, power, modulo=None):
        return '%d/%d' % (self.__num ** power, self.__den ** power)
    def __float__(self): 
        return self.__num / self.__den
    def __int__(self):
        return int(self.__float__())
    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)
frac = Fraction(7, 2)

print(frac)
print(~frac)
print(-frac)
print(frac**2)
print(float(frac))
print(int(frac))