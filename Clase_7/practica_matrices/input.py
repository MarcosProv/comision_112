# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from validaciones import *

def get_int(mensaje:str, mensaje_error:str, reintentos:int, minimo:int, maximo:int) -> int|None:
    for i in range(reintentos):
        numero = int(input(mensaje))
        if validate_number(minimo, maximo, numero):
            return numero
        else:
            print(mensaje_error)
