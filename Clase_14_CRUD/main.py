from Package.functions import *
from Package.empleados import *

opcion = None
while opcion != "I":
    opcion = input("A. Ingresar empleado\nB. Modificar empleado\nC. Eliminar empleado\nD. Mostrar todos\nE. Calcular salario promedio\n"\
                   "F. Buscar empleado por DNI:\nG. Ordenar empleados\n\n"\
                   "I. SALIR \n").upper()

    match opcion:
        case "A":
            ingresar_empleado()
        case "B":
            modificar_empleado(empleados_activos)
        case "C":
            eliminar_empleado()
        case "D":
            lista = elegir_archivo()
            mostrar_empleados(lista)
        case "E":
            print(calcular_promedio(empleados_activos))
        case "F":
            dni = get_int("Ingrese dni",3, 5000000 ,9999999)
            print(buscar(empleados_activos, "DNI", dni))
        case "G":
            ordenar_empleados(empleados_activos)
        case "I":
            opcion = "I"
    system("pause")
    system("cls")