c = 0
# esta funcion intecambia los valores de las variables a y b, sin perder informacion.
def swap(a: int, b: int):
    return b,a

# esta funcion ordena los numeros menores o iguales al pivote del lado izquierdo (o primeros)
# y va dejando a la derecha los mayores al pivote.

def particionar(array, low, high):
    pivote = array[high] #El pivote sera el ultimo elemento de la lista
    i = low - 1
        
    for j in range(low, high):
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = swap(array[i], array[j])
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] ) 

    return i + 1


def quick_sort(array, low, high):
    global c
    c += 1
# Utiliza un if para corroborar si el array esta correctamente ordenado y se encarga de cortar
# con la recursion.
    if low < high:
        pi = particionar(array, low, high)
# Esta funcion se encarga de llamarse recursivamente mientras que usa la funcion particionar
# para acomodar los numeros de la izquierda (1 y 3),
# y los de la derecha (5, 7 y 9).
        quick_sort(array, low, pi - 1)
#cuando el low llega a cero, esta otra funcion recursiva ordena los numeros del lado derecho de
#los primeros vectores
        quick_sort(array, pi + 1, high)
        

import time

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]

start = time.time()
# Se ejecuta la funcion quick_sort
quick_sort(vector, 0 , len(vector) - 1)
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")
print(c)
print(len(vector))
print(vector)

'''
¿Se les ocurre alguna forma de implementar el algoritmo sin utilizar recursión?
Sobre la implementación sin recursión, puedes usar un acumulador para simular la recursión de manera
iterativa. La idea es similar a cómo se haría con recursión, pero en lugar de llamar a la función recursivamente,
se agregan los índices de un acumulador. 

¿Notan diferencias en cuanto a performance?
Con la diferencia de rendimiento , la versión no recursiva puede ser más eficiente en términos de uso de memoria,
ya que no depende del sistema de llamadas recursivas de funciones. Pero en la práctica,
la diferencia de rendimiento puede ser mínima y depende del lenguaje de programación y del compilador utilizado.

'''

