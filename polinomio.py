from monomio import monomio

class polinomio:
    #Contructor de la clase polinomio. Asignamos la lista de monomios, la ordenamos y la simplificamos
    def __init__(self, lista):
        
        self.lista = lista
        self.ordenar()
        self.simplificar()      

    def __str__(self):
        if len(self.lista) == 0:
            return ""
        
        cadena = "".join([str(i) for i in self.lista]).strip()
        if cadena[0] == "+":
            cadena = " " + cadena[1:]
        
        return cadena

    #Ordenamos la lista de monomios mediante el método burbuja
    def ordenar(self):
        n = len(self.lista)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.lista[j].exponente > self.lista[j+1].exponente:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]
        
    #Simplificamos la lista de monomios uniendo los que tienen el mismo exponente en una nueva lista
    def simplificar(self):
        self.ordenar()
        self.lista.append(monomio(0,0))
        simplificado = []
        exponenteActual = self.lista[0].exponente
        listaAux = []
        for i in range(len(self.lista)):
            if self.lista[i].exponente != exponenteActual:
                monomioSimp = monomio(exponenteActual, 0)
                
                for j in listaAux:
                    monomioSimp = monomioSimp.suma(j)
                simplificado.append(monomioSimp)
                exponenteActual = self.lista[i].exponente
                listaAux = []
            listaAux.append(self.lista[i])
        self.lista = simplificado
    
    #Para sumar dos polinomios unimos las listas de monomios y las simplificamos
    def suma(self,otro):
        listaResultado = self.lista + otro.lista
        resultado = polinomio(listaResultado)
        resultado.simplificar()
        return resultado

    #Resta. 
    def resta(self, otro):
        listaResta = []
        listaA = self.lista.copy()
        listaB = otro.lista.copy()
        for i in range(0, len(listaA)):
            for j in range(0, len(listaB)):
                if listaA[i] == None or listaB[j] == None:
                    continue
                if listaA[i].exponente == listaB[j].exponente:
                    listaResta.append(listaA[i].resta(listaB[j]))
                    listaA[i] = None
                    listaB[j] = None
 
        listaResta = listaResta + listaA + listaB
        for i in listaResta:
            if i == None:
                listaResta.remove(i)
        return polinomio(listaResta)

    #Función para obtener el producto de dos listas de monomios
    def producto(self, otro):
        listaProducto = []

        for i in self.lista:
            for j in self.lista:
                listaProducto.append(i.producto(j))

        return polinomio(listaProducto)