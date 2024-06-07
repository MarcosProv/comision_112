# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from Package_Input.input import *
from .especificas import *

def pedir_10_numeros(lista:list) -> list:
    for i in range(len(lista)):
        numero = get_int("Ingresar un número entero entre -1000 y 1000. ", "dato no valido ", 10, -1000, 1000)
        lista[i] = numero
    return lista

def mostrar_cantidades_segun_signo(lista:list):
    cantidad_positivos = contar_cantidad_positivos(lista)
    cantidad_negativos = contar_cantidad_negativos(lista)
    print(f"los numeros positivos son {cantidad_positivos} y los negativos son {cantidad_negativos}")

def suma_pares(lista:list):
    acumulador = 0
    for i in range(len(lista)):
        if verificar_paridad(lista[i]):
            acumulador += lista[i]
    print(f"la suma es de {acumulador}")

def mostrar_mayor_par(lista:list):
    bandera_mayor = False
    for i in range(len(lista)):
        if verificar_paridad(lista[i])== None:
            if bandera_mayor == False or lista[i] > mayor:
                mayor = lista[i]
                bandera_mayor = True
    print(f"El mayor numero de los impares es {mayor}")

def listar_numeros(lista:list):
    for i in range(len(lista)):
        mensaje = f"El numero en la posicion {i} es {lista[i]}"
        print(mensaje)

def listar_numero_pares(lista:list):
    for i in range(len(lista)):
        if verificar_paridad(lista[i]):
            mensaje = f"El numero en la posicion {i} es {lista[i]}"
            print(mensaje)

def listar_posiciones_impares(lista:list):
    for i in range(len(lista)):    
        if verificar_paridad(i) == None:
            mensaje = f"El numero en la posicion {i} es {lista[i]}"
            print(mensaje)    
