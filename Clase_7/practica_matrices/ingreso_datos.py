# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from input import *
from validaciones import *

def cargar_linea_coche(tabla:list) -> list:
    linea = get_int("ingrese la linea del 1 al 3\n", "El numero esta fuera de rango\n", 5, 1,3) - 1             
    coche = get_int("ingrese un coche del 1 al 5\n", "El numero esta fuera de rango\n", 5, 1,5) - 1
    recuadacion = get_int("ingrese el valor recaudado\n", "Ingrese un numero mayor a cero y menor a 10.000\n", 5, 0, 9999)
    tabla[linea][coche] += recuadacion
    return tabla
 
def cargar_planilla(base_legajos:list, tabla:list, intentos:int) -> list | None:
    for _ in range(intentos):
        legajo = int(input("Ingrese su legajo\n"))
        if idententificarse(legajo, base_legajos):
            nueva_planilla = cargar_linea_coche(tabla)
            return nueva_planilla
        else:
             print("Error, chofer no identificado\n")