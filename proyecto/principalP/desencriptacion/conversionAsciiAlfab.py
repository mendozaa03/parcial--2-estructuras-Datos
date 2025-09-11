class AsciiTexto:
    def __init__(self,listaAscii):
        self.listaAscii = listaAscii
    def aTexto(self):
        return ''.join(chr(valor) for valor in self.listaAscii)
         