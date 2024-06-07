# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

def validar_tipo_int(numero: any)-> bool|None:
    if type(numero) == int:
        return True

##########################################################################################################

# Escribir una función que reciba una lista de enteros, la misma
# calculará y devolverá el promedio de todos los números.

def calcular_promedio(lista:list)->float:
    suma = 0 
    for i in range(len(lista)):
        if validar_tipo_int(lista[i]):
            suma += lista[i]
    promedio = suma / 2
    return promedio


# Escribir una función parecida a la anterior, pero la misma deberá
# calcular y devolver el promedio de los números positivos.

def calcular_promedio_positivos(lista:list)->float:
    suma = 0 
    for i in range(len(lista)):
        if validar_tipo_int(lista[i]) and lista[i] > 0:
            suma += lista[i]
    promedio = suma / 2
    return promedio


# Escribir una función que calcule y retorne el producto de todos
# los elementos de la lista que recibe como parámetro.

def calcular_producto(listalista:list)->int|None:
    producto = 1 
    for i in range(len(lista)):
        if validar_tipo_int(lista[i]):
            producto *= lista[i]
        return producto
    

# Escribir una función que reciba como parámetros una lista de
# enteros y retorne la posición del valor máximo encontrado.

def encontrar_maximo(lista):
    bandera = False
    for i in range(len(lista)):
        if bandera == False or lista[i] > maximo:
            bandera = True
            maximo = lista[i]
    return maximo
    


# Escribir una función que reciba como parámetros una lista de enteros
# y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def encontrar_maximo(lista:list) ->int:
    bandera_max = 0
    for i in range(len(lista)):
        if validar_tipo_int(lista[i]):
            if bandera_max == False or maximo < lista[i]:
                bandera_max = 1
                maximo = lista[i]
    return maximo

def mostrar_posiciones_enteros(lista):
    maximo = encontrar_maximo(lista)
    for i in range(len(lista)):
        if lista[i] == maximo:
            print(f"El maximo se encuentra en la posicion {i}")


# Escribe una función llamada reemplazar_nombres que reciba como
# parámetros una lista de nombres, un nombre a reemplazar y su
# correspondiente reemplazo. La función debe reemplazar cada
# ocurrencia del nombre a reemplazar en la lista con su correspondiente
# reemplazo y luego retornar la cantidad total de reemplazos realizados.

def reemplazar_nombres(lista_nombres, nombre_fuera, nombre_dentro):
    acumulador = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_fuera:
            lista_nombres[i] = nombre_dentro
            acumulador += 1
    # print(lista)
    return acumulador

lista = ["jose","Jorge","Jorge","Pablo","Miguel", "Jorge", "Gusman"]
resultado = reemplazar_nombres(lista, "Jorge", "Alejandro")
print(resultado)

