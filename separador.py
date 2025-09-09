class separar:
    def __init__(self,frase,fraseSeparada):
        self.frase = frase
        self.fraseSeparada = fraseSeparada


    def separador(self, frase, fraseSeparada):
        for palabra in  fraseSeparada: 
            for i in range(0,len(palabra)):
                print(palabra[i])