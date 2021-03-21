from monomio import monomio

class polinomio:
    f=open("input.txt", "r")

    lines = f.readlines()

    for line in lines:
        values = line.split(", ")
        print('exponente: {}, coeficiente: {}'.format(values[0], values[1]))
        

    print(f.read())
    print(monomio(1,3))