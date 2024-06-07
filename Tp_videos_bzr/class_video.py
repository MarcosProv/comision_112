from datetime import *
class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
    
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.colaborador}")
        print(f"Sesion: {self.sesion}")       
        print(f"Codigo: {self.codigo_url}")       
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento}")
        print("*"*30)

    def dividir_titulo(self):
        titulo = self.titulo.split(" | ")
        self.colaborador = titulo[0]
        self.sesion = titulo[1]

    def obtener_codigo_url(self):
        codigo = self.url_youtube.split("=")
        self.codigo_url = codigo[1]

    def formatear_fecha(self):
        self.fecha_lanzamiento = datetime.strptime(self.fecha_lanzamiento, '%Y-%m-%d')    

############### PUNTO A ##########################################################################################

    @staticmethod
    def normalizar_objetos(lista:list["Video"]) -> bool:
        for video in lista:
            video.dividir_titulo()
            video.obtener_codigo_url()
            video.formatear_fecha()
        return True

############### PUNTO B ##########################################################################################
    
    @staticmethod
    def mostrar_litsa_temas(lista:list["Video"]):
        for video in lista:
            video.mostrar_tema()

############### PUNTO C ##########################################################################################

    @staticmethod
    def obtener_numero_sesion(sesion:str) -> int:
        indice = sesion.index("#") + 1
        numero_sesion = int(sesion[indice:])
        return numero_sesion
    
    @staticmethod
    def ordenar_temas(lista:list["Video"]):
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if Video.obtener_numero_sesion(lista[i].sesion) > Video.obtener_numero_sesion(lista[j].sesion):
                    lista[i], lista[j] = lista[j], lista[i]

############### PUNTO D ##########################################################################################

    @staticmethod
    def calcular_promedio(lista:list["Video"]):
        acumulador = 0
        for video in lista:
            acumulador += video.vistas
        promedio = str(acumulador / len(lista))
        promedio = promedio.split(".")
        promedio = promedio[0]
        promedio = promedio.zfill(9)
        return promedio
    
    @staticmethod
    def construir_numero_k(promedio:str) -> str:
        numero_en_k =[]
        for i in range(len(promedio), 0, -3):
            numero_en_k.append(promedio[i-3:i])
        numero_en_k.reverse()
        union = ","
        resulado = union.join(numero_en_k)
        return resulado
    
    #las funciones no deben imprimir, solo retornar
    @staticmethod
    def mostrar_promedio_vistas(lista:list["Video"]):
        promedio = Video.calcular_promedio(lista)
        promedio = promedio.replace(".","")
        print(f"El promedio de reproducciones es de {Video.construir_numero_k(promedio)}")

############### PUNTO E ##########################################################################################

    @staticmethod
    def mostrar_mayor_visitas(lista:list["Video"]):
        bandera = False
        videos_mas_vistos = []

        for video in lista:
            if bandera == False or video.vistas >= numero_mayor:
                numero_mayor = video.vistas
                bandera = True

        for video in lista:
            if video.vistas == numero_mayor:
                videos_mas_vistos.append(video)
    
        for video in videos_mas_vistos:
            video.mostrar_tema()

############### PUNTO F ##########################################################################################
    
    @staticmethod
    def buscar_codigo(lista:list["Video"]):
        videos = []
        for video in lista:
            if video.codigo_url.find("nick") != -1:
                videos.append(video)
        Video.mostrar_litsa_temas(videos)

############### PUNTO G ##########################################################################################
    #las funciones no deben imprimir, solo retornar
    @staticmethod
    def buscar_colaborador(lista:list["Video"], colaboracion:str):
        videos = []
        for video in lista:
            artista = (video.colaborador).upper()
            if artista.find(colaboracion) != -1:
                videos.append(video)
        if videos:
            Video.mostrar_litsa_temas(videos)
        else:
            print("No hay videos del colaborador ingresado")

############### PUNTO H ##########################################################################################
    #las funciones no deben imprimir, solo retornar
    @staticmethod
    def buscar_mes(lista:list["Video"], mes:str):
        videos = []
        mes = mes.zfill(2)
        for video in lista:
            mes_video = (str(video.fecha_lanzamiento.month)).zfill(2)
            if mes_video == mes:
                videos.append(video)
        if videos:
            Video.mostrar_litsa_temas(videos)
        else:
            print("No hay videos del colaborador ingresado")