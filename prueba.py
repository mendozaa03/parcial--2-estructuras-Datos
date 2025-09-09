
from listaEnlazada import LinkedList
from listaEnlazada import Node
frase = "hola"
longitud = len(frase)
fraseSeparada= frase.split()
print(longitud)

contador = 0
listaLetras = []
linkedAscii = LinkedList()

for palabra in fraseSeparada:
    for i in range(0,len(palabra)):
        print(palabra[i])
        listaLetras.append(palabra[i])
        
print (listaLetras)

lista_ascii = [ord(letra) for letra in listaLetras]
print(lista_ascii)

#linkedAscii = [ord(letra) for letra in listaLetras]
#print(linkedAscii)





#contadorImpar = 1
#for impar in lista_ascii :
 #   for i in range (0,len(impar)):
  #      contadorImpar =+2
   #     print(contadorImpar)


#for hola in lista_ascii:
    #for i in range(0,size(hola)):
    #    contadorImpar =+ 2
        