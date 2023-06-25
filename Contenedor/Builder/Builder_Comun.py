from abc import ABC
from typing_extensions import override

from Contenedor.Builder.Builder import Builder


class BuilderComun(Builder, ABC):
    def __init__(self) -> None:
        pass
    
    @override
    def asignar_largo(self, largo):
        self.contenedor.set_largo(largo)
        return self
    
    @override
    def asignar_ancho(self, ancho):
        self.contenedor.set_ancho(ancho)
        return self

    @override
    def asignar_alto(self, alto):
        self.contenedor.set_alto(alto)
        return self
    
    @override
    def asignar_peso_max(self, peso_maximo):
        self.contenedor.set_peso_max(peso_maximo)
        return self
    
    @override
    def asignar_volumen(self, volumen):
        self.contenedor.set_volumen(volumen)
        return self

    @override
    def asignar_alto_exterior(self, alto_exterior):
        self.contenedor.set_alto_exterior(alto_exterior)
        return self
    
    @override
    def asignar_largo_exterior(self, largo_exterior):
        self.contenedor.set_largo_exterior(largo_exterior)
        return self

    @override
    def asignar_ancho_exterior(self, ancho_exterior):
        self.contenedor.set_ancho_exterior(ancho_exterior)
        return self
    
    @override
    def asignar_valor_adicional(self, valor_adicional):
        self.contenedor.set_valor_adicional(valor_adicional)
        return self
    
    @override
    def get_contenedor(self):
        return self.contenedor

    