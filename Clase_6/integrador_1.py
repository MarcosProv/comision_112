# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from Package_Arrays.array_Generales import *
from Package_Arrays.especificas import *
from os import system

lista_numeros = [0] * 10
bandera_seguir= True
bandera_lista_numeros = False

while bandera_seguir:
    opcion = int(input('''
1- Pedir el ingreso de 10 números enteros entre -1000 y 1000.
2- Mostrar la cantidad de números positivos y negativos.
3- Mostrar la sumatoria de los números pares.
4- Informar el mayor de los números impares.
5- Listar todos los números ingresados.
6- Listar todos los números pares.
7- Listar los números de las posiciones impares.
8 -Salir\n
'''))

    match opcion:
        case 1:
            if bandera_lista_numeros == False:
                lista_numeros = pedir_10_numeros(lista_numeros)
                bandera_lista_numeros = True
            else:
                print("Los numero ya estan ingresados")
        case 2:
            if bandera_seguir == True:
                mostrar_cantidades_segun_signo(lista_numeros)
        case 3:
            if bandera_seguir == True:
                suma_pares(lista_numeros)
        case 4:
            if bandera_seguir == True:
                mostrar_mayor_par(lista_numeros)
        case 5:
            if bandera_seguir == True:
                listar_numeros(lista_numeros)
        case 6:
            if bandera_seguir == True:
                listar_numero_pares(lista_numeros)
        case 7:
            if bandera_seguir == True:
                listar_posiciones_impares(lista_numeros)
        case 8:
            bandera_seguir = True  

    system("pause")
    system("cls")
