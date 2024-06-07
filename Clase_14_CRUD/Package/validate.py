# Nombre: Marcos
# Apellido: Provenzano
# Division: 112
from .empleados import empleados_activos

def formatear_num_k(numero):
    numero_formateado = "{:,}".format(numero)
    return numero_formateado

def preguntar(mensaje:str) -> bool:
    """
    Esta funcion necesita que el usuario ingrese 1 en caso de ser positivo y 2 en caso de ser negativo
    """    
    bandera = None
    while bandera == None:
        respuesa = input(mensaje).upper()
        if respuesa == "1":
            respuesa = True
            bandera = True
        elif respuesa == "2":
            respuesa = False
            bandera = True
        else:
            print("Por favor, ingrese 1 en caso de ser positivo y 2 en caso de ser negativo")
    return respuesa

def validar_cantidad_empleados():
    cantidad = True
    if len(empleados_activos) < 20:
        cantidad = True
    return cantidad

def validar_propio(mensaje):
    propio_bandera = True

    while propio_bandera:
        propio = str(input(f"{mensaje}\n"))
        if propio.isalpha() and len(propio) <= 20:
            propio_bandera = False
        elif propio.isalpha() == False:
            print("Asegurese de escribir solo caracteres alfabéticos, intente otra vez")
        elif len(propio) > 20:
            print("Se excedió el numero de caracteres, intente otra vez")

    propio = propio.capitalize()
    return propio

def get_int(mensaje, intentos, min, max = None):
    contador_intentos = 0
    while True:
        contador_intentos += 1
        if contador_intentos <= intentos:
            numero = str(input(f"{mensaje}\n"))
            if numero.isdigit():
                    if int(numero) >= min and (max == None or int(numero) <= max):
                        break
                    elif int(numero) < min:
                        print("El número es muy bajo, intente otra vez")
                    elif int(numero) > max:
                        print("El número muy alto, intente otra vez")
            else:
                print("Asegurese de escribir solo caracteres numéricos, intente otra vez")
        else:
            print("Se excedió el número de intentos")
            break
    return int(numero)
    
def obtener_puesto(mensaje):
    lista_puestos = ["A - Gerente", "B - Supervisor" ,"C - Analista" ,"D - Encargado","E - Asistente"]
    puesto = None
    while puesto == None:
        print(mensaje)
        for bacante in lista_puestos:
            print(bacante)
        respuesta = str(input())
        match respuesta.upper():
            case "A":
                puesto = "Gerente"
            case "B":
                puesto = "Supervisor"
            case "C":
                puesto = "Analista"
            case "D":
                puesto = "Encargado"
            case "E":
                puesto = "Asistente"
    return puesto
