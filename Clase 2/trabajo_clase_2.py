# Nombre: Marcos
# Apellido: Provenzano
# Division: 112


# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 

# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
   
# Escribe una función que calcule el área de un círculo. La función debe recibir el
# radio como parámetro y devolver el área.

# Crea una función que verifique si un número dado es par o impar. La función debe imprimir
# un mensaje indicando si el número es par o impar.

# Define una función que encuentre el máximo de tres números. La función debe
# aceptar tres argumentos y devolver el número más grande.

# Diseña una función que calcule la potencia de un número. La función debe recibir la
# base y el exponente como argumentos y devolver el resultado.

def perdir_numero()->int:
    """_summary_

    Returns:
        int: _description_
    """     
    numero = -1
    while numero < 0:
        numero = int(input("Ingrese un numero"))
    return numero

def perdir_numero_flotante()->float:
    numero = -1
    while numero < 0:
        numero = int(input("Ingrese un numero flotante"))
    return numero

def perdir_cadena()->str:
    texto = ""
    while texto == "":
        texto = str(input("ingrese un texto"))
    return texto

def calcular_area (radio:float) -> float:
    pi = 3.14
    area = pi*radio**2
    return area

def calcular_paridad(numero:int)->float:
    if numero%2 == 0:
        print ("El numero es par")
    else:
        print("El numero es impar")

def ecnontrar_num_max(num1:float, num2:float, num3:float)->float:
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3

def calcular_potencia(base:int, exponente:int)->int:
    resultado = base
    for i in range(exponente-1):
        base = resultado * base
    print(base)
