import random

def validar_repeticiones(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                if lista[j]==lista[i]:
                    return True

def crar_legajos(num):
    lista_legajos = [0]*num
    for i in range(len(lista_legajos)):
        lista_legajos[i] = random.randint(100,999)
    while validar_repeticiones(lista_legajos) == True:
        validar_repeticiones(lista_legajos)
    return lista_legajos

def crear_matriz_legajos(num):
    lista = crar_legajos(num)
    legajos = [[0]*5 for _ in range(3)]
    contador = 0
    for i in range(len(legajos)):
        for j in range(len(legajos[i])):
            legajos[i][j] = lista[contador]
            contador +=1 
    return legajos