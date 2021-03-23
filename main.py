from polinomio import polinomio
from monomio import monomio

lista = [monomio(4,2), monomio(1,9), monomio(5,3), monomio(7,8), monomio(0,4), monomio(3,0), monomio(3,-4), monomio(7,-4)]
p1 = polinomio(lista)
print(str(p1))
lista2 = [monomio(2,3), monomio(5,8), monomio(2,-4)]
p2 = polinomio(lista2)
print(str(p2))

p2.simplificar()
print(str(p2))
p1.simplificar()
print(str(p1))
print("llamo a suma")
print(str(p1.suma(p2)))