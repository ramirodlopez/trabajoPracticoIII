from Barco.Barco import Barco
from Contenedor.Contenedor import Contenedor
from Validacion_Barco.Validar_Subir_Al_Barco import Validar_Subir_Al_Barco


class Basico(Barco):
    
    def agregar_contenedor(self, contenedor: Contenedor):
        restriccion = Validar_Subir_Al_Barco()
        if(restriccion.verificar_restricciones_barco_basico(self, contenedor)):
            self._contenedores.add(contenedor)