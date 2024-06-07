from data import *
from os import system

respuesta = 0
opcion = 0

while respuesta != "A":
    respuesta = input(
    '''
A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.\n
    ''').upper()

Video.normalizar_objetos(lista_videos)

     
while opcion != "I":
    opcion = input(
    '''
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)\n
I. SALIR \n
    ''').upper()

    match opcion:
        case "B":
            Video.mostrar_litsa_temas(lista_videos)
        case "C":
            Video.ordenar_temas(lista_videos)
        case "D":
            Video.mostrar_promedio_vistas(lista_videos)
        case "E":
            Video.mostrar_mayor_visitas(lista_videos)
        case "F":
            Video.buscar_codigo(lista_videos)
        case "G":
            colaborador = ""
            while colaborador == "":
                colaborador = (input("ingrese un colaborador:\n")).upper()
            Video.buscar_colaborador(lista_videos, colaborador)
        case "H":
            mes = ""
            while mes == "":
                mes = input(
                '''
Ingrese el numero del mes:

01 - Enero
02 - Febrero
03 - Marzo
04 - Abril
05 - Mayo
06 - Junio
07 - Julio
08 - Agosto
09 - Septiembre
10 - Octubre
11 - Noviembre
12 - Diciembre
\n''').upper()
            Video.buscar_mes(lista_videos, mes)
        case "I":
            break

    system("pause")
    system("cls")