from Validacion_Barco.Validar_Subir_Al_Barco import Validar_Subir_Al_Barco
from excepcion.restriccion_excepcion import RestriccionException

class Validar_Subir_Al_Barco_Basico(Validar_Subir_Al_Barco):

    def verificar_restricciones_barco_segun_su_tipo(self, barco, contenedor):
        esValido = self.verificar_restricciones_barco_generales(barco, contenedor)

        if not self.es_basico(contenedor):
            esValido = False
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")
        
        if contenedor.is_especial():
            esValido = False
            raise RestriccionException("Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser \
                            transportado por un barco diseñado para tal fin.")
        
        return esValido
        