class monomio:

    #Constructor de la clase monomio
    def __init__(self, exponente, coeficiente):
        if exponente < 0:
            raise ValueError ("El exponente no debe ser negativo", exponente)
        else:
            self.exponente = exponente
            self.coeficiente = coeficiente

    #Función que llama a la clase monomio
    def __call__(self):
        return self

    #Función que permite imprimir un monomio
    def __str__(self):

        return str(self.coeficiente)+"x^"+str(self.exponente)+"\t"

    def suma(self, otro):
        if self.exponente != otro.exponente:
            raise ValueError ("Los exponentes deben coincidir")
        return monomio(self.exponente, self.coeficiente + otro.coeficiente)

    def __resta__(self, otro):
        if self.exponente != otro.exponente:
            raise ValueError("Los exponentes deben coincidir")
        return monomio(self.exponente, self.coeficiente + ~otro.coeficiente)
    
    def __producto__(self, otro):
        return monomio(self.exponente + otro.exponente, self.coeficiente * otro.coeficiente)

