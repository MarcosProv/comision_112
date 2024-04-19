# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from Package_Input.validate import get_int

# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

# Definición:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:

# En donde:
# número: el número ingresado por el usuario mediante consola, utilizando nuestra función get_int(mensaje,mensaje_error,mínimo,máximo,reintentos)


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
    numero_unidad = numero % 10
    numero_decena = numero // 10
    primer_numero = numero_decena % 10
    numero_centena = numero_decena % 10

    print(f"{numero_unidad} {primer_numero} {numero_centena}")

calcular_digitos(524)




#####################################################################################################################

# # Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir
# # el siguiente prototipo:


# def calcular_fibonacci(numero:int) -> int:
    # fibonachi = 0 
    # if fibonachi == numero:
        # resultado = fibonachi
        # return resultado
    # else:

