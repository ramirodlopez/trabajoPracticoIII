from typing_extensions import override
from Contenedor.Contenedor import Contenedor


class OpenTop(Contenedor):
    def __init__(self, id, especial) -> None:
        super().__init__(id, especial)    
        
    @override
    def entra_ancho(self, ancho_mercaderia):
        return self.get_ancho() >= ancho_mercaderia

    @override
    def entra_alto(self, alto_mercaderia):
        return True
    
    @override
    def valor_adicional(self):
        return self._valor_adicional