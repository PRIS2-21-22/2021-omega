from monomio import monomio

class polinomio:
    

    def __init__(self, lista):
        
        self.lista = lista
        #self.ordenar()
        #self.simplificar()
            

    def __str__(self):
        if len(self.lista) == 0:
            return ""
        
        cadena = "".join([str(i) for i in self.lista]).strip()
        if cadena[0] == "+":
            cadena = " " + cadena[1:]
        
        return cadena


    def ordenar(self):
        n = len(self.lista)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.lista[j].exponente > self.lista[j+1].exponente:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]
        

    def simplificar(self):
        self.ordenar()
        self.lista.append(monomio(0,0))
        simplificado = []
        expActual = self.lista[0].exponente
        listaAux = []
        for i in range(len(self.lista)):
            if self.lista[i].exponente != expActual:
                monomioSimp = monomio(expActual, 0)
                
                for j in listaAux:
                    monomioSimp = monomioSimp.suma(j)
                simplificado.append(monomioSimp)
                expActual = self.lista[i].exponente
                listaAux = []
            listaAux.append(self.lista[i])
        self.lista = simplificado
    

    def suma(self,otro):
        listaR = self.lista + otro.lista
        resultado = polinomio(listaR)
        resultado.simplificar()
        return resultado

    