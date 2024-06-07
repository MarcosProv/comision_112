# Nombre: Marcos
# Apellido: Provenzano
# Division: 112

class boligrafo:
    def __init__(self, grosor:str, color:str):
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor.upper()
        self.color = color.upper()
        self.cantidad_tinta = 80

    def escribir(self, texto):
        gasto = 0
        if self.grosor_punta == "FINO":
            gasto = 1
        elif self.grosor_punta == "GRUESO":
            gasto = 2
        tinta_usada = (len(texto)*gasto)

        if tinta_usada <= self.cantidad_tinta and tinta_usada > 0:
            self.cantidad_tinta = self.cantidad_tinta - tinta_usada
            cadena = texto
        elif tinta_usada > self.cantidad_tinta:
            cadena = "no alcanza la tinta"
        elif tinta_usada == 0:
            cadena = ""

        return cadena
    
    def recargar(self, cantidad:int):
        carga = self.cantidad_tinta + cantidad
        if carga > self.capacidad_tinta_maxima:
            sobrante = carga - self.capacidad_tinta_maxima
            self.cantidad_tinta = self.capacidad_tinta_maxima
            mensaje = f"Se recargó la lapicera y sobró {sobrante} de cantidad de tinta"
        else:
            self.cantidad_tinta = carga
            mensaje = "Se recargo la lapicera"
        return mensaje
