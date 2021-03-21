class monomio:

    #Constructor de la clase monomio
    def __init__(self, exponente, coeficiente):
        self.exponente = exponente
        self.coeficiente = coeficiente

    #Función que llama a la clase monomio
    def __call__(self):
        return self

    #Función que permite imprimir un monomio
    def __str__(self):
        return str(self.coeficiente)+"x^"+str(self.exponente)


