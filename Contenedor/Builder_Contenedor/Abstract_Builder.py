from abc import ABC, abstractmethod

class Builder(ABC): 
    
    @abstractmethod
    def reset(self, id, es_especial):
        pass
    
    @abstractmethod
    def get_contenedor(self):
        pass

    @abstractmethod
    def asignar_largo(self, largo):
        pass

    @abstractmethod
    def asignar_ancho(self, ancho):
        pass

    @abstractmethod
    def asignar_alto(self, alto):
        pass
    
    @abstractmethod
    def asignar_peso_max(self, peso_maximo):
        pass
    
    @abstractmethod
    def asignar_volumen(self, volumen):
        pass

    @abstractmethod
    def asignar_alto_exterior(self, alto_exterior):
        pass
    
    @abstractmethod
    def asignar_largo_exterior(self, largo_exterior):
        pass

    @abstractmethod
    def asignar_ancho_exterior(self, ancho_exterior):
        pass

