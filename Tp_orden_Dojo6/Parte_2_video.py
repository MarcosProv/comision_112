# Integrantes dojo 6 comisión 112:
#   Provenzano Marcos
#   Leone Teo
#   Ramiro di Fraia
#   Rodrigo Fleitas


vector = [5,3,4,8,7,5,1,2,3]

def ordenar_arreglo(arreglo):
    # pregunta si la lista llego a 1, de ser asi ya no se podra dividir y devuelve el arreglo
    if len(arreglo) <= 1:
        return arreglo
    # devuelve el indice por el cual se va a hacer el slice
    mitad = len(arreglo) // 2
    # Se hace el swap y el slice, quedando el arreglo dividido en dos mitades.
    derecha = arreglo[:mitad]
    izquierda = arreglo[mitad:]
    # Divide recursivamenrte la parte izquierda del arreglo
    izquierda = ordenar_arreglo(izquierda)
    # Divide recursivamenrte la parte derecha del arreglo
    derecha = ordenar_arreglo(derecha)
    # Llama recursivamentede a las funcion ordenar_arreglo, quien va a ordenar los numeros que
    # quedan al final y los retorna ordenados
    return ordenar_sub_arreglo(izquierda, derecha)

def ordenar_sub_arreglo(izquierda, derecha):
    resultado = []
    # Este ciclo va a iterar hasta que alguno de los dos arreglos quede en cero.
    # Mientras que el otro, siendo mayor, se indexara al final de el nuevo arreglo
    # "resultado" teniendo por delante los numeros menores que fueron comparandose.
    # Luego se indexa la otra lista, pero como estara vacia, no se veran cambios.

    while len(izquierda) > 0 and len(derecha) > 0:
        if izquierda[0] <= derecha[0]:
            # de ser valido se indexa al final
            resultado.append(izquierda[0])
            # la lista se recorta de uno en uno hasta que queda en cero
            izquierda = izquierda[1:]
        else:
            # de ser valido se indexa al final
            resultado.append(derecha[0])
            # la lista se recorta de uno en uno hasta que queda en cero
            derecha = derecha[1:]
    # el extend es similar al append, pero permite agregar varios elementos iterables.
    resultado.extend(izquierda)
    resultado.extend(derecha)
    return resultado

vector_2 = ordenar_arreglo(vector)

print(vector_2)

'''

5-Ventajas y Desventajas

Ventajas:

    Eficiencia: MergeSort tiene un tiempo de ejecución de O(n log n) 
    en todos los casos, lo que lo hace eficiente, especialmente para
    grandes conjuntos de datos.

    Estabilidad: Mantiene el orden relativo de los elementos con claves
    iguales, es util cuando se necesita preservar el orden original de
    los elementos.

    Versatilidad: Puede ser utilizado en diversos tipos de datos y
    estructuras, ya que no depende de comparaciones específicas.

Desventajas:

    Mucho uso de memoria: MergeSort requiere mucha memoria para
    almacenar los subarreglos durante la fusión, lo que puede ser
    una desventaja en sistemas con limitaciones de memoria.

    Complejidad de implementación e interpretacion: Su implementación es
    más compleja que otros algoritmos de ordenamiento como bubble sort o 
    insertion sort, ya que al ser un algoritmo recursivo, puede requerir
    más tiempo y habilidades para desarrollar y depurar el algoritmo.


6- Concordamos en que lo importante sobre el mergeSort es su eficiencia y
estabilidad. Aunque es más complejo de implementar que otros algoritmos de
ordenamiento no recursivos, como el bubble sort o el insertion sort, su
tiempo de ejecución es mucho más predecible y eficiente, especialmente para
conjuntos de datos grandes. Su reflexión radica en la comprensión profunda
de cómo funciona y en la apreciación de su elegancia al combinar y ordenar
de manera eficiente dos conjuntos ordenados en uno solo.

'''