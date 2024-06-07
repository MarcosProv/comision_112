# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from .empleados import empleados_activos, empleados_historico
from .validate import *
from os import system

################################################ FUNCIONES READ ##############################################################

def mostrar_empleados_id(empleados:list[dict]):
    for empleado in empleados:
        mensaje = "ID: " +  str(empleado["ID"]) + " -> "+ empleado["nombre"] + " " + empleado["apellido"]
        print(mensaje)

def pedir_id(empleados:list[dict]):
    bandera = None
    while bandera == None:
        mostrar_empleados_id(empleados)
        id = int(input("Ingrese in id:  "))
        for empleado in empleados:
            if empleado["ID"] == id:
                nombre = empleado["nombre"] + " " + empleado["apellido"]
                mensaje = f"\nEl empleado seleccionado es {nombre}\n"\
                           "Es correcto?\n 1 - SI   2 - No, salir\n" 
                respuesta = preguntar(mensaje)
                if respuesta == True:
                    print(id)
                    return id
                else:
                    bandera = True
                    break        

def elegir_archivo():
    repuesta = None
    while True:
        mensaje = "Elegir lista de empleados:\nA - Lista de empleados activos\nB - Lista de empleados antiguos\nC - Lista de ambos tipos de empleados"
        opcion = str(input(mensaje)).upper()
        match opcion:
            case "A":
                repuesta = empleados_activos
                break
            case "b":
                repuesta = empleados_historico
                break
            case "C":
                repuesta = empleados_activos + empleados_historico
                break
    return repuesta      

def mostrar_empleado(empleado):
    id = str(empleado["ID"])
    nombre = empleado["nombre"]
    aprellido = empleado["apellido"]
    dni = str(empleado["DNI"])
    puesto = empleado["puesto"]
    salario = empleado["salario"]

    separador = "|"
    empleado = f"{separador:10}{id:<20}{separador:10}{nombre:<20}{separador:10}{aprellido:<20}{separador:10}{dni:<20}"\
               f"{separador:10}{puesto:<20}{separador:10}{salario:<20}{separador:10}" 
    return empleado

def mostrar_empleados(lista:list[dict]):
    lista_empleados = lista
    claves = lista_empleados[0].keys()
    claves = list(claves)
    
    separador = "|"
    linea = "*"
    linea = (linea * 181)
    linea_guines = "-"
    linea_guines = (linea_guines * 181)

    tabla_arriba = f"{linea}\n"\
                   f"{separador:10}{claves[0].upper():<20}{separador:10}{claves[1].upper():<20}{separador:10}{claves[2].upper():<20}{separador:10}"\
                   f"{claves[3].upper():<20}{separador:10}{claves[4].upper():<20}{separador:10}{claves[5].upper():<20}{separador:10}\n"\
                   f"{linea_guines}"

    print(tabla_arriba)
    for empleado in lista_empleados:
        print(mostrar_empleado(empleado))
    print(linea)

def calcular_promedio(lista:list[dict]):
    acumulador = 0
    for empleado in lista:
        acumulador += empleado["salario"]
    promedio = acumulador / len(lista)
    return promedio
    
def buscar(lista:list[dict], clave:str, valor):
    encontrados = []
    for empleado in lista:
        for key in empleado:
            if key == clave:
                if empleado[clave] == valor:
                    encontrados.append(empleado)
    if encontrados:
        respuesa = encontrados
        mostrar_empleados(encontrados)
    else:
        respuesa = "No se encontro ningun empleado que coincida con la busqueda"
    return respuesa

################################################ FUNCIONES CREATE ##############################################################

ids = [len(empleados_activos)+ len(empleados_historico)]

def ingresar_empleado():
    if validar_cantidad_empleados():
        ids[0] = ids[0] + 1
        id = ids[0]
        nombre = validar_propio("Ingrese nombre")
        apellido = validar_propio("Ingrese apellido")
        dni = get_int("Ingrese dni",3, 5000000 ,9999999)
        dni = formatear_num_k(dni)
        salario = get_int("Ingrese salario",3 ,234315)
        salario = "$" + formatear_num_k(salario)
        puesto = obtener_puesto("ingrese el puesto")

        nuevo_empleado = crear_empleado(id, nombre, apellido, dni, puesto, salario)
        empleados_activos.append(nuevo_empleado)
        print("\n*** EL EMPLEADO SE INGRESO CORRECTAMENTE ***\n")
    else:
        print("Se alcanzo el limite de empleados")


def crear_empleado(id:int, nombre:str, apellido:str, dni:int, puesto:str, salario:float)-> dict:
    empleado = {
        "ID" : id,
        "nombre" : nombre,
        "apellido" : apellido,
        "DNI" : dni,
        "puesto" : puesto,
        "salario" : salario,
    }

    return empleado

def ordenar(lista:list[dict], modo, clave):
    if modo == "ascendente":
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i][clave] > lista[j][clave]:
                    lista[i], lista[j] = lista[j], lista[i]
    elif modo == "descendente":
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i][clave] < lista[j][clave]:
                    lista[i], lista[j] = lista[j], lista[i]

def ordenar_empleados(lista):
    mensaje = "Seleccione el dato de ordenamiento\nA - Nombre\nB - Apellido\nC - Salario\nD - Salir\n"
    mensaje2 = "Seleccione el tipo de ordenamiento\nA - Ascendente \nB - Descendente\n"
    while True:
        opcion = input(mensaje).upper()
        if opcion == "D":
            break
        opcion2 = input(mensaje2).upper()
        match opcion:
            case "A":
                if opcion2 == "A":
                    ordenar(lista,"ascendente", "nombre")
                    break
                elif opcion2 == "B":
                    ordenar(lista,"descendente", "nombre")
                    break
            case "B":
                if opcion2 == "A":
                    ordenar(lista,"ascendente", "apellido")
                    break
                elif opcion2 == "B":
                    ordenar(lista,"descendente", "apellido")
                    break
            case "C":
                if opcion2 == "A":
                    ordenar(lista,"ascendente", "salario")
                    break
                elif opcion2 == "B":
                    ordenar(lista,"descendente", "salario")
                    break
 
################################################ FUNCIONES UPDATE #############################################################

def modificar_empleado(lista:list[dict]):
    id = pedir_id(lista)
    for i in range(len(lista)):
        if id == lista[i]["ID"]:
            empleado_copia = lista[i].items()
            empleado_copia = dict(empleado_copia)
            respuesta = False
            mensaje = "Seleccione el dato a modificar\nA - Nombre\nB - Apellido\nC - Puesto\n"\
                      "D - Salario\nE - DNI\n" 
            while respuesta == False:
                opcion = input(mensaje).upper()
                match opcion:
                    case "A":
                        nombre = validar_propio("Ingrese nombre")
                        empleado_copia["nombre"] = nombre
                        respuesta = True
                    case "B":
                        apellido = validar_propio("Ingrese apellido")
                        empleado_copia["apellido"] = apellido
                        respuesta = True
                    case "C":
                        puesto = obtener_puesto("ingrese el puesto")
                        empleado_copia["puesto"] = puesto
                        respuesta = True
                    case "D":
                        salario = get_int("Ingrese salario",3 ,234315)
                        empleado_copia["salario"] = salario
                        respuesta = True
                        # salario = convertir_numero_k
                    case "E":
                        dni = get_int("Ingrese dni",3, 5000000 ,9999999)
                        empleado_copia["DNI"] = dni
                        respuesta = True

            lista_empleados_copia = [empleado_copia]
            mostrar_empleados(lista_empleados_copia)
            mensaje_confirmacion = f"¿Los datos son correctos?\n   1 - SI     2 - No, salir\n"
            cambiar = preguntar(str(mensaje_confirmacion))
 
            if cambiar:
                lista[i] = empleado_copia
                print("\n*** LOS DATOS SE ACTUALIZARON CORRECTAMENTE ***\n")


################################################ FUNCIONES DELETE #############################################################     

def eliminar_empleado():
    id = pedir_id(empleados_activos)
    for i in range(len(empleados_activos)):
        if id == empleados_activos[i]["ID"]:
            nombre = empleados_activos[i]["nombre"] + " " + empleados_activos[i]["apellido"]
            while True:
                mensaje = f"¿Esta seguro que desea eliminar a {nombre} de los empleados activos?\n  1 - SI     2 - No, salir\n"
                pregunta = preguntar(mensaje)
                if pregunta:
                        empleado_eliminado = empleados_activos.pop(i)
                        empleados_historico.append(empleado_eliminado)
                        return empleado_eliminado
                else:
                    break