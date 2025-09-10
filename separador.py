class separar:
    def __init__(self,frase,):
        self.frase = frase

    def fraseSeparada(self):
        return self.frase.split()

    def letrasPorPalabra(self):
        return [list(palabra) for palabra in self.palabras()]