# Nombre: Marcos
# Apellido: Provenzano
# Division: 112
from math import *

#region Calculos

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_perimetro_rectangulo(base, altura):
    perimetro = 2 * (base * altura)
    return perimetro
def calcular_area_circulo(radio:int) -> float:
    area = 3.1416 * (radio * radio)
    return area

def calcular_perimetro_circulo(radio:int) -> float:
    perimetro = 2 * 3.1416 * radio
    return perimetro

def calcular_area_triangulo_rectangulo(base, altura):
    area = base * altura / 2
    return area

def calcular_perimetro_triangulo_rectangulo(base, altura):
    hipotenusa = (base**2 + altura**2)**0.5
    perimetro = base + altura + hipotenusa
    return perimetro


#endregion

    
