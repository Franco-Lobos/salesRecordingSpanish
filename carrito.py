import pandas as pd
import time
import os
import datetime

compracliente = []
directorio = "/Users/francolobos/Desktop/Python/Pruebas/Parador/"
fecha = time.strftime("%""d_%m_%y")
header = "--NIMENIO" + 40*"-" + f"{fecha}--\n" + 60*"="

def mostrarproductos():
    print(header)
    df = pd.read_excel(f"{directorio}Productos.xlsx", engine = "openpyxl")
    print(df)
    return df

def cargaralcarrito(a):
    print(60*"=")
    seleccion = input("Seleccione el elemento que desea cargar al carrito\n")
    producto = (a.iloc[int(seleccion)])
    compracliente.append(producto)

def carritodecompras():
    while True:
        os.system("cls")
        productos = (mostrarproductos())
        cargaralcarrito(productos)
        cache = pd.DataFrame(compracliente)
        cache = cache.sort_values("Nombre").head()
        cache = cache.sort_values("Categoria").head()
        cache = cache.append({"Nombre" : " ", "Categoria" : "TOTAL", "Precio" : cache["Precio"].sum()}, ignore_index=True)
        print(cache)
        corte = input("\nIngrese \"fin\" para finalizar la compra\n")
        if corte == "fin":
            return cache

def nuevacompra(cliente, compranumero, condicionpago):
    pedido = pd.DataFrame(compracliente)
    compracliente.clear()
    pedido = pedido.sort_values("Nombre").head()
    pedido = pedido.sort_values("Categoria").head()
    pedido = pedido.append({"Nombre" : " ", "Categoria" : " ", "Precio" : 0}, ignore_index=True)
    pedido = pedido.append({"Nombre" : "Cliente", "Categoria" : f"{cliente.upper()}", "Precio" : 0}, ignore_index=True)
    pedido = pedido.append({"Nombre" : "Venta", "Categoria" : f"{compranumero}", "Precio" : 0}, ignore_index=True)
    pedido = pedido.append({"Nombre" : "Condición", "Categoria" : f"{condicionpago}", "Precio" : 0}, ignore_index=True)
    pedido = pedido.append({"Nombre" : " ", "Categoria" : "TOTAL", "Precio" : pedido["Precio"].sum()}, ignore_index=True)
    return pedido
