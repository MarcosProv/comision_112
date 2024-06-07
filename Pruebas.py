# c = 0

# def swap(a: int, b: int):
#     return b,a

# def particionar(array, low, high):
#     pivote = array[high] #El pivote sera el ultimo elemento de la lista
#     i = low - 1 #restamos uno para que no de fuera de rango
        
#     for j in range(low, high):
#         if array[j] <= pivote:
#             i += 1
#             array[i], array[j] = swap(array[i], array[j])
    
#     array[i + 1], array[high] = swap(array[i + 1], array[high] ) 

#     return i + 1

# def quick_sort(array, low, high):
#     global c
#     c += 1
#     if low < high:
#         pi = particionar(array, low, high)
#         quick_sort(array, low, pi - 1) #lo malo de esto es vuelve a ordenar lo que esta ordenado
#         quick_sort(array, pi + 1, high)
        

# import time
      
# vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,3]

# start = time.time()

# quick_sort(vector, 0 , len(vector) - 1)
           
# end = time.time()
# print(end)
# print(start)
# print(f"Tiempo: {(end - start)*1000}")
# print(c)
# print(len(vector))
# print(vector)

# '''
# ¿Se les ocurre alguna forma de implementar el algoritmo sin utilizar recursión?
# Sobre la implementación sin recursión, puedes usar un acumulador para simular la recursión de manera
# iterativa. La idea es similar a cómo se haría con recursión, pero en lugar de llamar a la función recursivamente,
# se agregan los índices de un acumulador. 

# ¿Notan diferencias en cuanto a performance?
# Con la diferencia de rendimiento , la versión no recursiva puede ser más eficiente en términos de uso de memoria,
# ya que no depende del sistema de llamadas recursivas de funciones. Pero en la práctica,
# la diferencia de rendimiento puede ser mínima y depende del lenguaje de programación y del compilador utilizado.

# '''

# nombres = ["marcos\n", "javier\n","dante\n"]
# for nombre in nombres:
#     print(nombre, end ="")

# fecha_cadena = "28/01/2023"
# fecha_objeto = datetime.strptime(fecha_cadena, "%d/%m/%Y")
# print(fecha_objeto)

numero = 1900500050

def formatear_num_k(numero):
    numero_formateado = "{:,}".format(numero)
    return numero_formateado
    
print(formatear_num_k(numero))
