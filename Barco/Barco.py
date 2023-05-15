from Contenedor.Contenedor import Contenedor
from Mercaderia.Mercaderia import Mercaderia
from abc import ABC, abstractmethod

class Barco(ABC):
    def __init__(self, id, cant_max_cont, peso_max_sopor, gps):
        self._id = id
        self._cant_max_cont = cant_max_cont
        self._peso_max_sopor = peso_max_sopor
        self._contenedores = set()
        self._peso = 0
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


    def get_peso(self):
        return self._peso

    def calcular_peso_cargado(self, contenedor: Contenedor):
        self._peso += contenedor.get_peso_ocupado()

    def cant_de_cont_cargado(self):
        return len(self._contenedores)

    @abstractmethod
    def agregar_contenedor(self, contenedor: Contenedor):
        pass

    def descargar_container(self):
        self._contenedores.clear()


    def validar_disenio(self, contenedor: Contenedor):
        es_basico = False
        if (contenedor.get_dim_ext_an() <= 2.45 and 
            contenedor.get_dim_ext_al() <= 2.6 and 
            contenedor.get_dim_ext_la() <= 6.1 and 
            contenedor.get_dim_int_an() <= 2.35 and 
            contenedor.get_dim_int_al() <= 2.3 and 
            contenedor.get_dim_int_la() <= 6.0):
            es_basico = True
        return es_basico
        

    def contenedor_con_material_especial(self, contenedor: Contenedor, mercaderia : Mercaderia):
        tiene_especial = False
        if(contenedor.tiene_materia_especial(mercaderia)):
             tiene_especial = True
        return tiene_especial


        
    #Ver lo del tema del viaje o del gps para saber el barco que recorrio la mayor y menor cantidad de KM