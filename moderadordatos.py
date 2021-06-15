import pandas as pd
import time
import os
import openpyxl

compracliente = []
directorio = "/Users/francolobos/Desktop/Python/Pruebas/"
fecha = time.strftime("%""d_%m_%y")
header = "--NIMENIO" + 40*"-" + f"{fecha}--\n" + 60*"="

def cajadeldia():
    nombre = fecha + ".xlsx"
    if nombre in os.listdir():
        existe = True
        return existe
    else:
        existe = False
        return existe

def datoscompra(cache):
    os.system("cls")
    print(header)
    print(cache)
    condicionpago = input("\nSeleccione la condición de pago:\n1)EFECTIVO\n2)TARJETA\n")
    if condicionpago == "1":
        condicionpago = "EFECTIVO"
    elif condicionpago == "2":
        condicionpago = "TARJETA" 
    else:
        datoscompra(cache)
    cliente = input("\nIngrese el nombre del cliente:\n")
    if cajadeldia() is False:
        compranumero = 1
        return cliente, compranumero, condicionpago
    else:
        reader = pd.ExcelWriter(f"{directorio}{fecha}.xlsx", mode = "r", engine = "openpyxl")
        ventasregsitro = openpyxl.load_workbook (f"{directorio}{fecha}.xlsx")
        ultimaventa = (ventasregsitro.get_sheet_names()[-1])
        compranumero = int(ultimaventa[6:]) + 1
        return cliente, compranumero, condicionpago

def metodoescritura(a):
    metodo = "w"
    if a in os.listdir():
        metodo = "a"
        return metodo
    return metodo

def registrarcompra(a,b):
    modo = metodoescritura(f"{fecha}.xlsx")
    writer = pd.ExcelWriter(f"{directorio}{fecha}.xlsx", mode = f"{modo}", engine = "openpyxl")
    a.to_excel(writer, f"VENTA {b}", index=False)
    writer.save()
