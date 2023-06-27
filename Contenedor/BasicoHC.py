from typing_extensions import override
from Contenedor.Basico import Basico

class BasicoHC(Basico):
    def __init__(self,id, especial):
        super().__init__(id, especial)
        
    @override
    def entra_ancho(self, ancho_mercaderia):
        return self.get_ancho() >= ancho_mercaderia
    
    @override
    def entra_alto(self, alto_mercaderia):
        return self.get_alto() >= alto_mercaderia
    
    @override
    def puede_contener_tipo_mercaderia(self, tipo_mercaderia):
        return False