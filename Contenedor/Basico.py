from typing_extensions import override

from contenedor.contenedor import Contenedor

class Basico(Contenedor):
    def __init__(self,id, especial):
        super().__init__(id, especial)
        self._alto = 2.3
        self._largo = 6.0
        self._ancho = 2.3
        self._peso_max = 24.000
        self._volumen = 32.6

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