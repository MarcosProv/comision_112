# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

def calcular_recuadacion_coche(tabla:list) -> int:
    total_coches = 0
    for i in range(len(tabla)):
       for j in range(len(tabla[i])):
           total_coches += tabla[i][j]
    return total_coches

def calcular_recaudacion_linea(tabla:list) -> int:
    total_lineas = [0] * 3
    for i in range(len(tabla)):
       for j in range(len(tabla[i])):
           total_lineas[i] += tabla[i][j]
    return total_lineas
