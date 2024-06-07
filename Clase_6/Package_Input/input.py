# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from .validate import validate_number, validate_length

###################################################################################################################

# 1) Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

def get_int(mensaje:str, mensaje_error:str, reintentos:int, minimo:int, maximo:int) -> int|None:
    for i in range(reintentos):
        numero = int(input(mensaje))
        if validate_number(minimo, maximo, numero):
            return numero
        else:
            print(mensaje_error)

# get_int("introduce un entre 5 y 10 ", "El numero no es valido ", 5, 5, 10)

'''
def get_int(mensaje:str, mensaje_error:str, reintentos:int, minimo:int, maximo:int) -> int|None:
    acumulador = 0
    while acumulador < reintentos:
        numero = int(input(mensaje))
        if numero < minimo or numero > maximo:
           print(mensaje_error)
           acumulador += 1
        else:
            return numero
    return False 
'''     

###################################################################################################################

# 2) Teniendo en cuenta la función del punto 1, crear la función get_string.

def get_string(longitud:int, mensaje:str, mensaje_error:str, reintentos:int) -> str|None:
    for i in range(reintentos):
        texto = str(input(mensaje))
        if validate_length(texto, longitud):
            return texto
        else:
            print(mensaje_error)

# get_string(5, "introduce un texto de 5 caracteres ", "El texto no es valido ", 5)

'''
def get_string(longitud:int, mensaje:str, mensaje_error:str, reintentos:int) -> str|None:
    acumulador = 0
    while acumulador < reintentos:
        texto = str(input(mensaje))
        if len(texto) < longitud or len(texto) > longitud:
            acumulador += 1
            print(mensaje_error)
        else:
            return texto
    return None
'''

###################################################################################################################

# 3)
def get_float(mensaje:str, mensaje_error:str, reintentos:int, minimo:float, maximo:float) -> float|None:
    acumulador = 0
    while acumulador < reintentos:
        numero = float(input(mensaje))
        if numero < minimo or numero > maximo:
           print(mensaje_error)
           acumulador += 1
        else:
            return numero
    return False 