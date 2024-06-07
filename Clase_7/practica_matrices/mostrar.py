# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from calculos import *

def mostrar_recaudacion_total(tabla:list) -> None:
    total = calcular_recuadacion_coche(tabla)
    mensaje = f"El total recaudado es de ${total}"
    print(mensaje)

def mostrar_recuadacion_linea(tabla:list) -> None:
    total_lineas = calcular_recaudacion_linea(tabla)
    mensaje = f"La primera linea recaudo ${total_lineas[0]}\n"\
              f"La segunda linea recaudo ${total_lineas[1]},\nY la tercera recuado ${total_lineas[2]}"
    print(mensaje)

def mostrar_recuadacion_coche_linea(tabla:list) -> None:
    total_coches = calcular_recuadacion_coche(tabla)
    total_lineas = calcular_recaudacion_linea(tabla)
    mensaje = f"La recuadacion de todos los coches fue de ${total_coches}\nLa primera linea recaudo ${total_lineas[0]}\n"\
              f"La segunda linea recaudo ${total_lineas[1]},\nY la tercera recuado ${total_lineas[2]}"
    print(mensaje)

def mostrar_recuadacion_coche(tabla:list) -> None:
     for i in range(len(tabla)):
          for j in range(len(tabla[i])):
               mensaje = f"El coche {j+1}, de la linea {i+1} recuado ${tabla[i][j]}"
               print(mensaje)
