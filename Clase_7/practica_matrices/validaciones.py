# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

def validate_number(minimo:int, maximo:int, numero: int) -> bool:
    if numero >= minimo and numero <= maximo:
           return True

def idententificarse(legajo:int, base_legajos:list) -> bool:
    for i in range(len(base_legajos)):
            for j in range(len(base_legajos[0])):
                if base_legajos[i][j] == legajo:
                    return True