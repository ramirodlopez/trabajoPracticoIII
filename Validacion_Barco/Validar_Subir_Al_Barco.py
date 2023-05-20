
from excepcion.restriccion_excepcion import RestriccionException


class Validar_Subir_Al_Barco(Exception):

    def verificar_restricciones_barco_generales(self, barco, contenedor):
        es_valido = True

        if not barco.validar_cant_container():
            es_valido = False
            barco._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar más containers del máximo definido")
            

        if not barco.validar_peso():
            es_valido = False
            barco._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar más peso del máximo definido")
        
        return es_valido
    

    def verificar_restricciones_barco_basico(self, basico, contenedor):

        es_valido = self.verificar_restricciones_barco_generales(basico, contenedor)

        if not basico.es_basico(contenedor):
            es_valido = False
            basico._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")
        
        if contenedor.is_especial():
            es_valido = False
            basico._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser \
                            transportado por un barco diseñado para tal fin.")
        
        return es_valido
        

    def verificar_restricciones_barco_avanzado(self, avanzado, contenedor):

        es_valido = self.verificar_restricciones_barco_generales(avanzado, contenedor)
        
        if not avanzado.es_avanzado(contenedor):
            avanzado._peso_total-= contenedor.get_peso_ocupado()
            es_valido = False
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")
        
        return es_valido