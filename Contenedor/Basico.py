from Contenedor.Contenedor import Contenedor
from typing_extensions import override

class Basico(Contenedor):
    def __init__(self,id, especial):
        super().__init__(id, especial)
        self._ancho = 2.35
        self._alto = 2.3
        self._largo = 6.0
        self._peso_max = 24000
        self._volumen = 32.42999999999999
        self._ancho_exteriror = 2.45
        self._alto_exteriror = 2.6
        self._largo_exteriror = 6.1

    @override
    def entra_ancho(self, ancho_mercaderia):
        return self._ancho >= ancho_mercaderia
    
    @override
    def entra_alto(self, alto_mercaderia):
        return self._alto >= alto_mercaderia
    
    def get_alto(self):
        return self._ancho    
    
    def get_ancho(self):
        return self._ancho   
    
    def get_ancho_exterior(self):
        return self._ancho_exteriror