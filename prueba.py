#este archivo netamente lo cree para hacer pruebas durante la clase, ya despues le aplique la implemetacion de clases POO 
#la cree para llevar una idea de como crear los metodos en las clases y no comenzar a la deriva



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


sumaImpar = [valor + (2*n + 1) for n, valor in enumerate(lista_ascii)]
print(sumaImpar)


for valor in sumaImpar:
    linkedAscii.Append(valor)

print(linkedAscii)
linkedAscii.Remove()
