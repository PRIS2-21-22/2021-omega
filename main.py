from polinomio import polinomio
from monomio import monomio

lista = [monomio(4,2), monomio(1,9), monomio(5,3), monomio(7,8), monomio(0,4), monomio(3,0), monomio(3,-4), monomio(7,-4)]
p1 = polinomio(lista)
print("Polinomio 1:")
print(str(p1))
lista2 = [monomio(2,3), monomio(5,8), monomio(2,-4)]
p2 = polinomio(lista2)
print("Polinomio 2:")
print(str(p2))
print("Suma:")
print(str(p1.suma(p2)))
print("Resta:")
print(str(p1.resta(p2)))
print("Producto:")
print(str(p1.producto(p2)))