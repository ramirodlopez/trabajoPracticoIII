from Contenedor.Contenedor import Contenedor
from typing_extensions import override

class Basico(Contenedor):
    def __init__(self,id, especial):
        super().__init__(id, especial)

    @override
    def entra_ancho(self, ancho_mercaderia):
        return self._ancho >= ancho_mercaderia
    
    @override
    def entra_alto(self, alto_mercaderia):
        return self._alto >= alto_mercaderia
    
    @override
    def valor_adicional(self):
        return 0.0