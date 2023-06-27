from Contenedor.Contenedor import Contenedor
from Estrategia.Estrategia import Estrategia
from Pedido.Pedido import Pedido
from Validacion_Barco.Validar_Subir_Al_Barco import Validar_Subir_Al_Barco

class Barco():
    def __init__(self, id, cant_max_cont, peso_max_sopor, gps):
        self._id = id
        self._cant_max_cont = cant_max_cont
        self._peso_max_sopor = peso_max_sopor
        self._contenedores = set()
        self._peso_total = 0
        self._gps = gps
        self._tanque = None
        self._estrategia = None
        self._hora_activacion_estrategia = []
        self._horas_motor = 0 
        self.hora_llegada_barco = 0

    def set_hora_llegada(self, hora_llegada):
        self.hora_llegada_barco = hora_llegada

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

    def set_estrategia(self, estrategia: Estrategia):
        self._estrategia = estrategia

    def set_capacidad_tanque(self, tanque):
        self._tanque = tanque

    def get_peso_total(self):
        return self._peso_total
    
    def get_contenedores(self):
        return self._contenedores
    
    def get_horas_activacion_estrategia(self):
        return self._hora_activacion_estrategia
    

    def get_capacidad_tanque(self):
        return self._tanque

    def calcular_peso_cargado(self, contenedor: Contenedor):
        self._peso_total += contenedor.get_peso_ocupado()

    def contar_contenedores(self):
        return len(self._contenedores)
    
    def agregar_contenedor(self, contenedor: Contenedor, restriccion: Validar_Subir_Al_Barco):
        if(restriccion.verificar_restricciones_barco_segun_su_tipo(self, contenedor)):
            self._contenedores.add(contenedor)
            self.calcular_peso_cargado(contenedor)

    def descargar_container(self):
        self._contenedores.clear()


    def obtener_ganacia_barco(self, pedido: Pedido):
        ganancia_barco = 0
        for contenedor_actual in self.get_contenedores():
            ganancia_barco += contenedor_actual.obtener_ganancia_contenedor(pedido)
        return ganancia_barco
    

    def do_something(self):
        self._estrategia.hora_de_activacion()


    def cargar_horas_activacion_estrategia(self, estrategia: Estrategia):
        self._hora_activacion_estrategia.append(estrategia)
        

    def set_horas_usadas(self):
        i = len(self._hora_activacion_estrategia) - 1
        uso_motor = 0
        if(self._hora_activacion_estrategia[i].get_tipo() == "Motor"):
            uso_motor = self.hora_llegada_barco - self._hora_activacion_estrategia[i].hora_activacion()
        
        while(i > 0):

            if(self._hora_activacion_estrategia[i].get_tipo() == "Motor"):
                uso_motor += self._hora_activacion_estrategia[i].hora_activacion() - self._hora_activacion_estrategia[i - 1].hora_activacion()

            i = i - 1

        self._horas_motor = uso_motor
            