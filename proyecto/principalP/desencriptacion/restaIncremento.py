class restaImpares : 
    def __init__(self, listaModificada):
        self.listaModificada = listaModificada
    
    def restarImpares(self):
        return [valor - (2*n +1) for n, valor in enumerate(self.listaModificada) ]
         