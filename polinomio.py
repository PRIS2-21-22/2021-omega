from monomio import monomio

class polinomio:
    

    def __init__(self, lista):
        f=open("input.txt", "r")
        self.lista = lista
        lines = f.readlines()

        for line in lines:
            values = line.split(", ")
            #print('exponente: {}, coeficiente: {}'.format(values[0], values[1]))
            lista.append(monomio(values[0],values[1]))
            

    def __str__(self):
        cadena=""
        for i in range(len(self.lista)):
            cadena+=(str(lista[i])+"\t")
        return cadena

    def __suma__(self, otro):
        #TODO

    def __resta__(self, otro):
        #TODO

    def __producto__(self,otro):
        #TODO
        


lista = []
p1 = polinomio(lista)
print(polinomio(lista))
print("===============================")
for x in range(len(p1.lista)):
    print(p1.lista[x].exponente,p1.lista[x].coeficiente)
