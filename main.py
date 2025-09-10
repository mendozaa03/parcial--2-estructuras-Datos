import random
from api import obtenerFrases
from separador import separar
from conversionAscci import conversion
from incremento import incremento
from listaEnlazada import LinkedList
from collections import deque


arrayDeque = deque()

def main():
    frases = obtenerFrases()
    cantidad_frases = len(frases)  


    numeroFrases = random.randint(1, cantidad_frases)
    print(f"Se procesarán {numeroFrases} frases aleatorias")

    frases_elegidas = random.sample(frases, numeroFrases)

    for frasesEncriptadas in frases_elegidas:
        print(f"\nFrase a encriptar: {frasesEncriptadas}")
        separado = separar(frasesEncriptadas)
        for palabra in separado.fraseSeparada():
            asciiConvertido = conversion(palabra)
            listaAscii = asciiConvertido.to_ascii()
            incrementos = incremento(listaAscii)
            sumaImpar = incrementos.sumaImpares()
            linkedAscii = LinkedList()
            for valor in sumaImpar:
                linkedAscii.Append(valor)
            linkedAscii.intercambiarAdyacente() 
            arrayDeque.append(linkedAscii) # encriptar la linked list de frases al array dequeu

    for palabra_encriptada in arrayDeque:
        print(palabra_encriptada)
   


if __name__ == "__main__":
    main()
