from Validacion_Barco.Validar_Subir_Al_Barco import Validar_Subir_Al_Barco
from excepcion.restriccion_excepcion import RestriccionException

class Validar_Subir_Al_Barco_Avanzado(Validar_Subir_Al_Barco):

    def verificar_restricciones_barco_segun_su_tipo(self, barco, contenedor):
        esValido = self.verificar_restricciones_barco_generales(barco, contenedor)
        
        if not self.es_avanzado(contenedor):
            esValido = False
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")
        
        return esValido