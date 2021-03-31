#from sympy import *
import sympy as sp


x=sp.Symbol('x')

b0=sp.Symbol('b0')
b1=sp.Symbol('b1')
b2=sp.Symbol('b2')
b3=sp.Symbol('b3')
b4=sp.Symbol('b4')
b5=sp.Symbol('b5')

print ("%s"%sp.simplify(b0 + x*(b1 + x*(b2 + x*(b3 + x*(b4 + x*b5))))))

print ("%s"%sp.expand(b0 + x*(b1 + x*(b2 + x*(b3 + x*(b4 + x*b5))))))


x0=sp.Symbol('x0')
x1=sp.Symbol('x1')
x2=sp.Symbol('x2')
y0=sp.Symbol('y0')
y1=sp.Symbol('y1')
y2=sp.Symbol('y2')

exp = sp.simplify((y1-y0)/(x1-x0) + (y2-y1)/(x2-x1))
print ("%s"%exp)
exp = sp.expand((y1-y0)/(x1-x0) + (y2-y1)/(x2-x1))
print ("%s"%exp)
