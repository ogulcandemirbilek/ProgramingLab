"""
1'den 21'e kadar olan sayıların torbadan çekilişini yapıyoruz. Torbadan çekilen sayının asal sayı olma olasılığını hesaplıyoruz.
"""
from sympy import FiniteSet
from fractions import Fraction

t = FiniteSet(1,2,3)
s = FiniteSet(2,4,6)

if t == s:
    print("True")
else:
    print("False")

print(t.union(s))
print(t.intersect(s))
print(t**2) 

def probability (space, event): 
    return len(event) / len(space)
    # space, örneklem uzayını belirtir. event ise belirli bir olayı belirtir.

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

space = FiniteSet(* range(1, 21))
# * operatörü ile range içindeki aralıkta bulunan tüm değerler kümeye eleman olarak aktarılır.

primes = []
for num in space:
    if check_prime(num):
        primes.append(num)
# Örnek uzayımızdaki asalları belirler ve primes dizisine atarız.

event = FiniteSet(* primes)
p = probability(space, event)

print("Sample space: ", space)  # Örneklem uzayı
print("Event: ", event)         # Belirli bir olay / Gelen sayının asal olma durumu
print('Probability of event: {0:.3f}'.format(p))  # Olayın gerçekleşme olasılığı
