# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

def encontrar_subcadena(cadena:str,subcadena:str)-> bool:
    verdad = False 
    largo = len(subcadena)
    for i in range(len(cadena)):
        if cadena[i:i+largo] == subcadena:
            verdad = True
            break
    return verdad

sospechosos =["Juan Pérez","María Rodríguez","Carlos Sánchez"]
muestras = ["CGGGGCTAAAATTTTTTACGATCG","AACGTTTAATGTTCTAAGCTGCG","CGGGGCTAAAATTTTTTACGATCG"]
prueba = "CGTTTAATG"

for i in range(len(sospechosos)):
    if encontrar_subcadena(muestras[i],prueba):
        print(f"El asesino es {sospechosos[i]}")

