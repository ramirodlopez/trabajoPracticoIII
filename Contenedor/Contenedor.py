from typing import List
from abc import ABC, abstractmethod
from mercaderia.mercaderia import Mercaderia
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

    def cargar_mercaderia(self, mercaderia: Mercaderia):
        mercaderia.verificar_restricciones(self)
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
    
    def get_ancho(self):
        return self._ancho
    
    def get_largo(self):
        return self._largo
    
    def get_peso_max(self):
        return self._peso_max
    
    def get_peso_ocupado(self):
        return self._peso_ocupado

    def get_volumen(self):
        return self._volumen

    def get_volumen_ocupado(self):
        return self._volumen_ocupado

    def esta_completo(self):
        return self._completo

    def get_mercaderias(self) -> List[Mercaderia]:
        return self._mercaderias
    

    
    

