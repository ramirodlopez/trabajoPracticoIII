from typing_extensions import override
from Contenedor.Contenedor import Contenedor
from trabajoPracticoIII.Mercaderia.Tipo_Mercaderia import TipoMercaderia

class Alimenticio(Contenedor):
    def __init__(self, id, especial) -> None:
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
    
    @override
    def puede_contener_tipo_mercaderia(self, tipo_mercaderia):
        return TipoMercaderia.ALIMENTICIO == tipo_mercaderia