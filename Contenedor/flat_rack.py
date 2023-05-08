from typing_extensions import override

from contenedor.contenedor import Contenedor
'''
 * Este contenedor no tiene ancho, por ende hereda directamente de {@link Container}.
'''
class FlatRack(Contenedor):
    def __init__(self,id, especial):
        super().__init__(id, especial)
        self._largo = 6.0
        self._pesoMax = 45000
        self._volumen = 33
    
    '''
     * Entra a lo alto porque no tiene techo.
    '''
    @override
    def entra_alto(self, alto_mercaderia):
        return True
    
    @override
    def entra_ancho(self, ancho_mercaderia):
        return True