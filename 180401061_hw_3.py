
#Oğulcan Demirbilek 180401061 
#Github : https://github.com/ogulcandemirbilek
#binomial distrubition :n sayıda iki kategori (yani başarı/başarısızlık, evet/hayır, 1/0 vb) sonucu veren denemelere uygulanır. Örenk olarak, 10 kere atılan madeni paranın 6 tane yazı gelme olasılığı, 1000 kişinin hasta olup olmama olasılığı, 100 yeni doğan bebeğin erkek/kız olma olasılığı vb. 
#binom dağılımı formulü : P(x) = Combination(n,x)*p**x*(1-p)**(n-x)
import sympy as sym
from sympy import Symbol
from sympy import pprint
import sympy.plotting as syp
import matplotlib.pyplot as plt
p = Symbol('p') # p; istenilen durumu başarma olasılığı
x = Symbol('x') # x; istenilen durum sayısı
n = Symbol('n') # n; deneme sayısı
part_1 = sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
part_2 = p**x
part_3 = (1-p)**(n-x)
my_binomial_function = part_1*part_2*part_3
syp.plot(my_binomial_function.subs({p:0.6,n:120}),(x,0,70),title = 'Binomial Distrubition plot for n= 120')
x_value =[]
y_value =[]
for value in range(0,71):
    y = my_binomial_function.subs({p:0.6,n:120,x:value})
    x_value.append(value)
    y_value.append(y)
plt.plot(x_value,y_value)
plt.show()
