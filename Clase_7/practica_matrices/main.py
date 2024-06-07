# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from matriz_aleatoria import *
from os import system
from ingreso_datos import *
from mostrar import *

bander_salida = True

m_legajos = crear_matriz_legajos(15)


planilla = [[0]*5 for _ in range(3)]

while bander_salida:
    opcion = int(input('''
1- Cargar planilla.
2- Mostrar la recaudación de todos los coches y líneas.
3- Calcular y mostrar recaudación por línea.
4- Calcular y mostrar recaudación por coche.
5- Calcular y mostrar la recaudación total.
6- Salir\n
'''))
    match opcion:
            case 1:
                cargar_planilla(m_legajos, planilla, 5)
                print(m_legajos)
            case 2:
                mostrar_recuadacion_coche_linea(planilla)
            case 3:
                mostrar_recuadacion_linea(planilla)
            case 4:
                mostrar_recuadacion_coche(planilla)
            case 5:
                mostrar_recaudacion_total(planilla)
            case 6:
                bander_salida = False

    system("pause")
    system("cls")