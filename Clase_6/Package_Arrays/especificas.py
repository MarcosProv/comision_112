# Nombre: Marcos
# Apellido: Provenzano
# Division: 112


def contar_cantidad_positivos(lista:list) -> int:
    contador = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            contador += 1
    return contador

def contar_cantidad_negativos(lista:list) -> int:
    contador = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            contador += 1
    return contador

def verificar_paridad(numero:int) -> bool:
    if numero % 2 == 0:
        return True