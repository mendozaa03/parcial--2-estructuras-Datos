class incremento : 
    def __init__(self,listaAscii):
        self.listaAscii = listaAscii

    def sumaImpares(self):
        return [valor + (2*n+1) for n, valor in enumerate(self.listaAscii)]


