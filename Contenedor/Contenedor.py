from typing import List
from abc import ABC, abstractmethod

from excepcion.restriccion_excepcion import RestriccionException

class Contenedor(ABC):
    def __init__(self, id, especial) ->None:
        self._id = id
        self._especial = especial
        self._largo = None
        self._peso_max = 0.0
        self._peso_ocupado = 0.0 
        self._volumen = 0.0
        self._volumen_ocupado = 0.0 
        self._completo = False
        self._mercaderias = []
        self._alto_exterior = 0.0
        self._largo_exterior = 0.0
    

    def cargar_mercaderia(self, mercaderia, verificar_restriccion_mercaderia):
        verificar_restriccion_mercaderia.verificar_restricciones(self)
        self._mercaderias.append(mercaderia)
        self._peso_ocupado += mercaderia.get_peso()
        self._volumen_ocupado += mercaderia.devolver_volumen()
        self.verificar_completo()
    
    def verificar_completo(self):
        if (self._peso_ocupado == self._peso_max):
            self._completo = True
        
        if (self._volumen_ocupado == self._volumen):
            self._completo = True
    

    def esta_completo_con_unica_carga(self) -> bool:
        return self._completo and len(self._mercaderias) == 1

    @abstractmethod
    def entra_ancho(self, ancho_mercaderia):
        pass

    @abstractmethod
    def entra_alto(self, alto_mercaderia):
        pass

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def is_especial(self):
        return self._especial
    
    def get_largo(self):
        return self._largo
    
    def get_peso_max(self):
        return self._peso_max
    
    def get_peso_ocupado(self):
        return self._peso_ocupado

    def set_peso_ocupado(self, valor):
        self._peso_ocupado = valor

    def get_volumen(self):
        return self._volumen

    def get_volumen_ocupado(self):
        return self._volumen_ocupado
    
    def set_volumen_ocupado(self, valor):
        self._volumen_ocupado = valor

    def esta_completo(self):
        return self._completo

    def get_mercaderias(self) -> List:
        return self._mercaderias
    
    def get_alto_exterior(self):
        return self._alto_exterior
    
    def get_largo_exterior(self):
        return self._largo_exterior
    
    def get_ancho_exterior(self):
        return self._ancho_exterior


    def verificar_restricciones_barco_generales(self, barco):
        es_valido = True

        if not barco.validar_cant_container():
            es_valido = False
            barco._peso_total-= self.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar más containers del máximo definido")
            

        if not barco.validar_peso():
            es_valido = False
            barco._peso_total-= self.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar más peso del máximo definido")
        
        return es_valido
    

    def verificar_restricciones_barco_basico(self, basico):

        es_valido = self.verificar_restricciones_barco_generales(basico)

        if not basico.es_basico(self):
            es_valido = False
            basico._peso_total-= self.get_peso_ocupado()
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")
        
        if self.is_especial():
            es_valido = False
            basico._peso_total-= self.get_peso_ocupado()
            raise RestriccionException("Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser \
                            transportado por un barco diseñado para tal fin.")
        
        return es_valido
        

    def verificar_restricciones_barco_avanzado(self, avanzado):

        es_valido = self.verificar_restricciones_barco_generales(avanzado)
        
        if not avanzado.es_avanzado(self):
            avanzado._peso_total-= self.get_peso_ocupado()
            es_valido = False
            raise RestriccionException("Un barco no puede cargar un container para el cual no fue diseñado.")
        
        return es_valido

    

