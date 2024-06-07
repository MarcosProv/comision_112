# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

def validar_tipo_int(numero: any)-> bool|None:
    """_summary_
    Returns:
        bool: Valida si el dato es de tipo int
    """    
    if type(numero) == int:
        return True

