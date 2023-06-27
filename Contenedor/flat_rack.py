from typing_extensions import override

from Contenedor.Contenedor import Contenedor
class FlatRack(Contenedor):
    def __init__(self,id, especial):
        super().__init__(id, especial)
                
    @override
    def entra_alto(self, alto_mercaderia):
        return True
    
    @override
    def entra_ancho(self, ancho_mercaderia):
        return True
    
    
    @override
    def puede_contener_tipo_mercaderia(self, tipo_mercaderia):
        return False