# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def perdir_numero()->int:     
    numero = -1
    while numero < 0:
        numero = int(input("Ingrese un numero"))
    return numero

# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def perdir_numero_flotante()->float:
    numero = -1
    while numero < 0:
        numero = int(input("Ingrese un numero flotante"))
    return numero

# Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
def perdir_cadena()->str:
    texto = ""
    while texto == "":
        texto = str(input("ingrese un texto"))
    return texto

# Escribe una función que calcule el área de un círculo. La función debe recibir el
# radio como parámetro y devolver el área.

def calcular_area (radio:float) -> float:
    pi = 3.14
    area = pi*radio**2
    return area


# Crea una función que verifique si un número dado es par o impar. La función debe imprimir
# un mensaje indicando si el número es par o impar.

def calcular_paridad(numero:int)->float:
    if numero%2 == 0:
        print ("El numero es par")
    else:
        print("El numero es impar")
        

# Define una función que encuentre el máximo de tres números. La función debe
# aceptar tres argumentos y devolver el número más grande.

def ecnontrar_num_max(num1:float, num2:float, num3:float)->float:
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3
    

# Diseña una función que calcule la potencia de un número. La función debe recibir la
# base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base:int, exponente:int)->int:
    resultado = base
    for i in range(exponente-1):
        base = resultado * base
    print(base)
