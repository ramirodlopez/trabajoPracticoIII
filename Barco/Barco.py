from Contenedor.Contenedor import Contenedor
from abc import ABC, abstractmethod

class Barco(ABC):
    def __init__(self, id, cant_max_cont, peso_max_sopor, gps):
        self._id = id
        self._cant_max_cont = cant_max_cont
        self._peso_max_sopor = peso_max_sopor
        self._contenedores = set()
        self._peso_total = 0
        self._gps = gps

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_cant_max_cont(self):
        return self._cant_max_cont

    def set_cant_max_cont(self, cant_max_cont):
        self._cant_max_cont = cant_max_cont

    def get_peso_max_sopor(self):
        return self._peso_max_sopor

    def set_peso_max_sopor(self, peso_max_sopor):
        self._peso_max_sopor = peso_max_sopor

    def get_gps(self):
        return self._gps
    
    def set_gps(self, gps):
        self._gps = gps


    def get_peso_total(self):
        return self._peso_total
    
    def get_contenedores(self):
        return self._contenedores

    def calcular_peso_cargado(self, contenedor: Contenedor):
        self._peso_total += contenedor.get_peso_ocupado()

    def contar_contenedores(self):
        return len(self._contenedores)

    @abstractmethod
    def agregar_contenedor(self, contenedor: Contenedor):
        pass

    def descargar_container(self):
        self._contenedores.clear()

    def es_basico(self, contenedor: Contenedor):
        basico = False
        if (contenedor.get_ancho_exterior() == 2.45 and 
            contenedor.get_alto_exterior() == 2.6 and 
            contenedor.get_largo_exterior() == 6.1):
            basico = True
        return basico
    
    def es_avanzado(self, contenedor: Contenedor):
        avanzado = False
        if (contenedor.get_ancho_exterior() > 2.45 and 
            contenedor.get_alto_exterior() > 2.6 and 
            contenedor.get_largo_exterior() > 6.1):
            avanzado = True
        return avanzado
    
    def validar_cant_container(self):
        cant_valida = False
        if(self.contar_contenedores() <= self._cant_max_cont):
            cant_valida = True
        return cant_valida
    
    def validar_peso(self):
        peso_valido = False
        if(self.get_peso_total() <= self.get_peso_max_sopor()):
            peso_valido = True
        return peso_valido