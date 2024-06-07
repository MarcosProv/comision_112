# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from Package_Input.input import get_int

# Realizar una función recursiva que calcule la suma de los primeros números naturales: 
def sumar_naturales(numero:int) -> int:
    if numero == 0:
        resultado = numero
    else:
        numero = numero + sumar_naturales(numero - 1)
        resultado = numero
    return resultado

# print(sumar_naturales(5))

#####################################################################################################################

# Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base:int, exponente:int) -> int:
    resultado = base
    if exponente == 1:
        resultado = base
    else:
        resultado = calcular_potencia(resultado, exponente -1) * base
    return resultado

# print(calcular_potencia(2,5))

#####################################################################################################################

# Realizar una función recursiva que la suma de los dígitos de un número:

def calcular_digitos(numero:int):
    if numero < 10:
        return numero
    else:
        primeros_digitos = numero // 10
        suma_digitos = (numero % 10) + calcular_digitos(primeros_digitos)
    return suma_digitos

digitos = get_int("Lntroduce un numero mayor a cero para calcular la suma de sus digitos ", "El numero no es valido ", 5, 1, 99999)

# suma_digitos = calcular_digitos(digitos)
# print(f"La suma es de {suma_digitos}")
# 

#####################################################################################################################

# # Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir
# # el siguiente prototipo:

def calcular_fibonacci(numero):
    if numero <= 1:
        return numero
    else:
        resultado = (calcular_fibonacci(numero - 1)) + (calcular_fibonacci(numero - 2))
    return resultado

# numero = get_int("introduce un entre 5 y 10 ", "El numero no es valido ", 5, 5, 10)
# fibonacci = calcular_fibonacci(numero)
# print(fibonacci)