from typing_extensions import override

from Contenedor.Contenedor import Contenedor
class FlatRack(Contenedor):
    def __init__(self,id, especial):
        super().__init__(id, especial)
        self._largo = 6.0
        self._pesoMax = 45000
        self._volumen = 33
        self._alto_exteriror = 2.3
        self._largo_exteriror = 6.1
        
    @override
    def entra_alto(self, alto_mercaderia):
        return True
    
    @override
    def entra_ancho(self, ancho_mercaderia):
        return True