from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
p = x*(x+x)
#print(p)

from sympy import factor,expand
expr = (x**2)-(y**2)
factors = factor(expr)
expands = expand(factors)
#print(factors,expands)

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
#print(factors)

from sympy import pprint
#pprint(factors)

x = Symbol('x')
series = x
n=5
for i in range(2,n+1):
    series  = series + (x**i)/i
#pprint(series)

expr = x*x+x*y+x*y+y*y
res = expr.subs({x:1,y:2})
#print(res)
r = expr.subs({x:y-1})
#print(r)

x = Symbol('x')
series = x
n=5
x_values=10
for i in range(2,n+1):
    series  = series + (x**i)/i
#pprint(series)
series_values = series.subs({x:x_values})
#print(series_values)

import sympy as sym
import sympy.plotting as syp
sigma = Symbol('sigma')
mu = Symbol('mu')
x = Symbol('x')
part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gauss_function = part_1*part_2
#pprint(my_gauss_function)
syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='Gauss distrubition')

x_value =[]
y_value = []
for value in range(-10,10):
    y = my_gauss_function.subs({mu:1,sigma:3,x:value}).evalf()
    x_value.append(value)
    y_value.append(y)
    print(value,y)
import matplotlib.pyplot as plt
plt.plot(x_value,y_value)
plt.show()


