# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

# 1 Crear una función que reciba como parámetro una cadena y determine
# la cantidad de vocales que hay de cada una (individualmente).
# La función retornará una matriz indicando en la columna 1 cada vocal,
# y en la columna 2 la cantidad.

def averiguar_vocal(cadena:str) -> list:
    matriz =[["a","e","i","o","u"],
             [0,0,0,0,0]]

    for i in range(len(cadena)):
       letra = cadena[i]
       match ord(letra):
           case 97 | 65:
               matriz[1][0] += 1
           case 101 | 69:
               matriz[1][1] += 1
           case 101 | 69:
               matriz[1][2] += 1
           case 111 | 79:
               matriz[1][3] += 1
           case 117 | 85:
               matriz[1][4] += 1
    return matriz
            
# Crear una función que reciba una cadena y un caracter. La función deberá
# devolver el índice en el que se encuentre la primera incidencia de dicho
# caracter, o -1 en caso de que no esté.

def encontrar_incidencia(texto:str,caracter:str) -> int:
    intice = -1
    for i in range(len(texto)):
        if texto[i] == caracter:
            intice = i
            break
    return intice

# Crear una función que reciba como parámetro una cadena y determine si
# la misma es o no un palíndromo. Deberá retornar un valor booleano indicando
# lo sucedido.

def indicar_palindromo(texto:str) -> bool:
    texto_reves = ""
    palindromo = False
    for i in range(len(texto), -1,-1):
        texto_reves = texto_reves + texto[i:i+1]
    if texto_reves == texto:
        palindromo = True
    return palindromo


# Crear una función que reciba como parámetro una cadena y suprima los
# caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def eliminar_repetidos(texto:str) -> str:
    i = 1
    texto_nuevo =""
    for i in range(len(texto)):
        if texto[i] != texto[i-1]:
            texto_nuevo = texto_nuevo + texto[i]
    print(texto_nuevo)

# Crear una función que reciba una cadena por parámetro y suprima las vocales
# de la misma.

def preguntar_vocal(letra:str)-> bool:
    estado = False
    vocales = [97, 65, 101, 69, 101, 69, 111, 79, 117, 85]
    for vocal in vocales:
        if vocal == ord(letra):
            estado = True
    return estado            

def suprimir_vocales(texto:str) -> str:
    nuevo_texto = ""
    for i in range(len(texto)):
        if not preguntar_vocal(texto[i]):
            nuevo_texto += texto[i]
    return nuevo_texto

# Crear una función para contar cuántas veces aparece una subcadena dentro
# de una cadena.

def econtrar_subcadena(cadena:str,subcadena:str)-> bool:
    contador = 0 
    largo = len(subcadena)
    for i in range(len(cadena)):
        if cadena[i:i+largo] == subcadena:
            contador +=1
    return contador
