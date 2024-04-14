# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

total_empleados = 10

nombre = ""
edad = 0
genero = ""
tecnologia = ""

empleados_masculinos_iot_ia = 0
empleados_no_ia = 0

edades_masculinas = []
nombres_masculinos = []
tecnologias_masculinas=[]

edad_maxima = 0

for i in range(total_empleados):
    edad = 0
    nombre = input("Ingrese su nombre: ")
    while edad < 18:
        edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su genero (Masculino - Femenino - Otro): ")
    genero = genero.upper()
    tecnologia = input("Ingrese su tecnologia ((IA, RV/RA, IOT): ")
    tecnologia = tecnologia.upper()

    if genero == "MASCULINO" and edad >= 25 and edad <= 50:
        if tecnologia == "IA" or tecnologia == "IOT":
            empleados_masculinos_iot_ia += 1

    if tecnologia != "IA":
        if genero != "FEMENINO" or edad > 33 and edad < 40:
            empleados_no_ia += 1

    if genero == "MASCULINO":
            edades_masculinas.append(edad)
            nombres_masculinos.append(nombre)
            tecnologias_masculinas.append(tecnologia)

porcentaje = empleados_no_ia * 100 / total_empleados


respuesta_1 = f"La cantidad de empleados de género masculino que votaron por IOT o IA,"\
              f"cuya edad esté entre 25 y 50 años inclusive, es de {empleados_masculinos_iot_ia}"

respuesta_2 = f"El porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino"\
              f"o su edad se encuentre entre los 33 y 40, es de {porcentaje}%"

print(f"{respuesta_1}\n{respuesta_2}")


for i in range(len(edades_masculinas)):
        if edades_masculinas[i] >= edad_maxima:
            edad_maxima = edades_masculinas[i]

for i in range(len(edades_masculinas)):
     if edades_masculinas[i] == edad_maxima:
        print(f"{nombres_masculinos[i]} es uno de los mayores con una edad de {edad_maxima} años y su tecnologia es {tecnologias_masculinas[i]}")