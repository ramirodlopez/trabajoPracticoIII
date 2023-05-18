from Barco.Barco import Barco
from Contenedor.Contenedor import Contenedor


class Basico(Barco):
    
    def agregar_contenedor(self, contenedor: Contenedor):

        if(contenedor.verificar_restricciones_barco_basico(self)):
            self._contenedores.add(contenedor)