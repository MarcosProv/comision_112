# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

from Grafico import *
from os import *

def inicio_programa():
    while True:
        opcion = int(input("1. Seleccionar figura y cargar valores\n2. Visualizar resultados\n3. Salir\nElija una opción: "))
        match opcion:
            case 1:
                print("¿Qué tipo de figura desea representar?")
                que_figura = input("a. Círculo\nb. Rectángulo\nc. Triángulo\nd. Volver al menu anterior\nElija una opción: ")
                match que_figura:
                    case "a":
                        color = seleccionar_color("Elija un color\n")
                        radio = int(input("Introduzca el radio:\n"))
                        posicion_x = int(input("Introduzca posición en X:\n"))
                        posicion_y = int(input("Introduzca posición en y:\n"))
                        posicion =(posicion_x, posicion_y)
                        system("cls")
                        figura = {
                            "figura" : "Circulo",
                            "posicion" : posicion,
                            "color" : color,
                            "radio" : radio,
                            "dimensiones" : radio
                                }
                        print(figura)
                    case "b":
                        color = seleccionar_color("Elija un color\n")
                        base = int(input("Introduzca la base:\n"))
                        altura = int(input("Introduzca la altura:\n"))
                        posicion_x = int(input("Introduzca posición en X:\n"))
                        posicion_y = int(input("Introduzca posición en y:\n"))
                        posicion =(posicion_x, posicion_y)
                        system("cls")
                        figura = {
                            "figura" : "Rectangulo",
                            "posicion" : posicion,
                            "color" : color,
                            "dimensiones" : (base, altura)
                                }
                    case "c":
                        color = seleccionar_color("Elija un color\n")
                        base = int(input("Introduzca la base:\n"))
                        altura = int(input("Introduzca la altura:\n"))
                        posicion_x = int(input("Introduzca posición en X:\n"))
                        posicion_y = int(input("Introduzca posición en y:\n"))
                        posicion =(posicion_x, posicion_y)
                        system("cls")
                        figura = {
                            "figura" : "Triangulo",
                            "posicion" : posicion,
                            "color" : color,
                            "dimensiones" : (base, altura)
                                }
                    case "d":
                        pass
            case 2:
                graficar(figura)
            case 3:
                print("Gracias por usar nuestro programa")
                break 
        system("cls")

inicio_programa()