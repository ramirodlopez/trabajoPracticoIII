from abc import ABC, abstractmethod

from excepcion.restriccion_excepcion import RestriccionException


class Validar_Subir_Al_Barco(ABC):
    def es_basico(self, contenedor):
        return (
            contenedor.get_ancho_exterior() == 2.45 and
            contenedor.get_alto_exterior() == 2.6 and
            contenedor.get_largo_exterior() == 6.1
        )

    
    def es_avanzado(self, contenedor):
        return (
            contenedor.get_ancho_exterior() > 2.45 and
            contenedor.get_alto_exterior() > 2.6 and
            contenedor.get_largo_exterior() > 6.1
        )
    
    def validar_cant_container(self, barco):
        return barco.contar_contenedores() <= barco._cant_max_cont
    
    def validar_peso(self, barco, contenedor):
        return barco.get_peso_total() + contenedor.get_peso_ocupado() <= barco.get_peso_max_sopor()

    def verificar_restricciones_barco_generales(self, barco, contenedor):
        esValido = True

        if not self.validar_cant_container(barco):
            esValido = False
            raise RestriccionException("Un barco no puede cargar más containers del máximo definido")
            
        if not self.validar_peso(barco, contenedor):
            esValido = False
            raise RestriccionException("Un barco no puede cargar más peso del máximo definido")
        
        return esValido
    

    @abstractmethod
    def verificar_restricciones_barco_segun_su_tipo(self, barco, contenedor):
        pass