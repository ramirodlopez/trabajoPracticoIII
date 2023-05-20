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
        self._ancho_exterior = 0.0
    

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
    
    def set_especial(self, especial):
        self._especial = especial
    
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
    
    def set_alto_exterior(self, alto_exterior):
        self._alto_exterior = alto_exterior
    
    def get_largo_exterior(self):
        return self._largo_exterior
    
    def set_largo_exterior(self, largo_exterior):
        self._largo_exterior = largo_exterior
    
    def get_ancho_exterior(self):
        return self._ancho_exterior
    
    def set_ancho_exterior(self, ancho_exterior):
        self._ancho_exterior = ancho_exterior
        return self._ancho_exterior


