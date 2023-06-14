
from excepcion.restriccion_excepcion import RestriccionException


class Validar_Subir_Al_Barco(Exception):
    def es_basico(self, contenedor):
        basico = False
        if (contenedor.get_ancho_exterior() == 2.45 and 
            contenedor.get_alto_exterior() == 2.6 and 
            contenedor.get_largo_exterior() == 6.1):
            basico = True
        return basico
    
    def es_avanzado(self, contenedor):
        avanzado = False
        if (contenedor.get_ancho_exterior() > 2.45 and 
            contenedor.get_alto_exterior() > 2.6 and 
            contenedor.get_largo_exterior() > 6.1):
            avanzado = True
        return avanzado
    
    def validar_cant_container(self, barco):
        cant_valida = False
        if(barco.contar_contenedores() <= barco._cant_max_cont):
            cant_valida = True
        return cant_valida
    
    def validar_peso(self, barco):
        peso_valido = False
        if(barco.get_peso_total() <= barco.get_peso_max_sopor()):
            peso_valido = True
        return peso_valido

    def verificar_restricciones_barco_generales(self, barco, contenedor):
        if not self.validar_cant_container(barco):
            barco._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar más containers del máximo definido")
            
        if not self.validar_peso(barco):
            barco._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar más peso del máximo definido")
    

    def verificar_restricciones_barco_basico(self, barco, contenedor):
        self.verificar_restricciones_barco_generales(barco, contenedor)

        if not self.es_basico(contenedor):
            barco._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")
        
        if contenedor.is_especial():
            barco._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser \
                            transportado por un barco diseñado para tal fin.")
        

    def verificar_restricciones_barco_avanzado(self, barco, contenedor):
        self.verificar_restricciones_barco_generales(barco, contenedor)
        
        if not self.es_avanzado(contenedor):
            barco._peso_total-= contenedor.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")