from Contenedor.Basico import Basico

class BasicoHC(Basico):
    def __init__(self,id, especial):
        super().__init__(id, especial)
        self._alto = 2.3
        self._largo = 12.0
        self._ancho = 2.35
        self._peso_max = 32.500
        self._volumen = 67.7
        self._ancho_exteriror = 2.45
        self._alto_exteriror = 2.6
        self._largo_exteriror = 12.1