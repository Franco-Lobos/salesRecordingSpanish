import pandas as pd
import time
import os
import sys
import carrito
import moderadordatos

compracliente = []
directorio = "/Users/francolobos/Desktop/Python/Pruebas/"
fecha = time.strftime("%""d_%m_%y")
header = "--NIMENIO" + 40*"-" + f"{fecha}--\n" + 60*"="

def compraintegral():
    os.system("cls")
    cache = carrito.carritodecompras()
    datos = (moderadordatos.datoscompra(cache))
    comprafinal = carrito.nuevacompra(datos[0], datos[1], datos[2])
    moderadordatos.registrarcompra(comprafinal, datos[1])
    os.system("cls")
    print(header)
    print(comprafinal, "\n\nLa compra ha sido cargada con éxito!")
    time.sleep(5)


while True:
    compraintegral()
