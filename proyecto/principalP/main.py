import random
from proyecto.principalP.api.api import obtenerFrases
from proyecto.principalP.encriptacion.separador import separar
from proyecto.principalP.encriptacion.conversionAscci import conversion
from proyecto.principalP.encriptacion.incremento import incremento
from proyecto.principalP.encriptacion.listaEnlazada import LinkedList
from collections import deque
from proyecto.principalP.desencriptacion.conversionAsciiAlfab import AsciiTexto
from proyecto.principalP.desencriptacion.restaIncremento import restaImpares
from proyecto.principalP.logs import get_logger
import time
import psutil


logger = get_logger()
arrayDeque = deque()

def main():
    
    logger.info("inicio del proceso de seleccion de frases y encriptacion")
    proceso = psutil.Process()

    try:
        
        tiempoTotalInicio=time.time()
        memInicial = proceso.memory_info().rss
        cpuInicial = proceso.cpu_percent(interval=None)
        logger.info(f"memoria inicial : {memInicial/(1024*2):.2f} MB // cpu inicial : {cpuInicial:.2f}%")
        frases = obtenerFrases()
        cantidad_frases = len(frases)
      
        numeroFrases = random.randint(1, cantidad_frases)
        logger.info(f"Se procesarán {numeroFrases} frases aleatorias")
        frases_elegidas = random.sample(frases, numeroFrases)


        tiempoEncripIn = time.time()
        for frasesEncriptadas in frases_elegidas:
            logger.info(f"\nFrase a encriptar: {frasesEncriptadas}")
            print("========================================================================")
            separado = separar(frasesEncriptadas)
            for palabra in separado.fraseSeparada():
                try:
                    logger.debug(f"palabra:,{palabra}")
                    asciiConvertido = conversion(palabra)
                    listaAscii = asciiConvertido.to_ascii()
                    logger.debug(f"ascii: {listaAscii}")
                    incrementos = incremento(listaAscii)
                    sumaImpar = incrementos.sumaImpares()
                    logger.debug(f"suma de impares aplicada {sumaImpar}")
                    linkedAscii = LinkedList()
                    for valor in sumaImpar:
                        linkedAscii.Append(valor)
                    linkedAscii.intercambiarAdyacente() 
                    logger.debug(f"palabra encriptada como lista enlazada y con intercambio de adyacentes: {linkedAscii}")
                    arrayDeque.append(linkedAscii) # encriptar la linked list de frases al array dequeu
                except Exception as e:
                    logger.error("error encriptando")

        tiempoEncripFin = time.time()
        logger.info(f"encriptacion finalizada y guardada. tiempo: {(tiempoEncripFin - tiempoEncripIn):.4f} segundos")
        logger.info("========================================================================")
        logger.info("procediendo con proceso de desencriptacion \n ")
        print("========================================================================")

        #desencriptando

        tiempoDesencriptIn =time.time()
        for linkedAscii in arrayDeque:
            try:
                linkedAscii.intercambiarAdyacente()
                valores_modificados = []
                current = linkedAscii.First
                while current:
                    valores_modificados.append(current.value)
                    current = current.next
                resta = restaImpares(valores_modificados)
                valores_originales = resta.restarImpares()

                ascii_a_texto = AsciiTexto(valores_originales)
                texto = ascii_a_texto.aTexto()
                logger.info(f"texto desencriptado: {texto}")
            except Exception as e: 
                logger.error("error desencriptando palabras")
        
        tiempoDesencriptFin = time.time()
        logger.info(f"desencriptacion completada. tiempo: {(tiempoDesencriptFin - tiempoDesencriptIn):.4f} segundos")
        
        #performance
        memoriaFinal = proceso.memory_info().rss
        cpuFinal = proceso.cpu_percent(interval=None)
        logger.info(f"memoria final : {memoriaFinal/(1024**2):.2f} MB // Cpu final : {cpuFinal:.2f} %")
        logger.info(f"diferencia de memoria: {(memoriaFinal - memInicial) / (1024**2):2.f} MB")

        
        
        tiempoTotalFin = time.time()
        logger.info(f"Tiempo total duranta la ejecucion del programa: {(tiempoTotalFin - tiempoTotalInicio):.4f} segundos")
        logger.info("fin del proceso")
    except Exception as e:
        logger.critical("error")

    print("==========================================")




if __name__ == "__main__":
    main()
