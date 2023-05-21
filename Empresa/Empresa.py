class Empresa():
    def __init__(self, barcos, contenedores):
        self.__barcos = barcos
        self.__contenedores = contenedores
        self.__viajes = []
        self.__pedidos = []
       

    def agregar_viaje(self, viaje):
        self.__viajes.append(viaje)

    def agregar_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def get_viajes(self) -> list:
        return self.__viajes

    def get_pedidos(self) ->list:
        return self.__pedidos

    def get_barcos(self) ->list:
        return self.__barcos

    def get_contenedosres(self) -> list:
        return self.__contenedores    
    
    def obtener_contenedor_mayor_cantidad_viajes_completo_unica_carga(self):
        id_contenedor_a_cantidad_viajes = {}
        for viaje in self.__viajes:
            if (viaje.get_estado() == "FINALIZADO"):
                nuevo_id_contenedor_a_cantidad_viajes = self.actualizar_cantidad_viajes_contenedor(viaje, id_contenedor_a_cantidad_viajes)
                if (nuevo_id_contenedor_a_cantidad_viajes != None):
                    id_contenedor_a_cantidad_viajes = nuevo_id_contenedor_a_cantidad_viajes
        id_contenedor_max_viajes = max(id_contenedor_a_cantidad_viajes, key=id_contenedor_a_cantidad_viajes.get)
        return self.buscar_contenedor_por_id(id_contenedor_max_viajes)
    

    def actualizar_cantidad_viajes_contenedor(self, viaje, id_contenedor_a_cantidad_viajes):
        barco = viaje.get_barco()
        for contenedor in barco.get_contenedores():
            if (contenedor.esta_completo_con_unica_carga()):
                self.aumentar_contador_viajes_contenedor(id_contenedor_a_cantidad_viajes, contenedor)


    def aumentar_contador_viajes_contenedor(self, id_contenedor_a_cantidad_viajes, contenedor):
        cantidad_viajes = id_contenedor_a_cantidad_viajes.get(contenedor.get_id())
        if cantidad_viajes is None:
            id_contenedor_a_cantidad_viajes[contenedor.get_id()] = 1
        else:
            cantidad_viajes += 1
            id_contenedor_a_cantidad_viajes[contenedor.get_id()] = cantidad_viajes

    def buscar_contenedor_por_id(self, id_contendedor_max_viajes):
        for contenedor in self.__contenedores:
            if (contenedor.get_id() == id_contendedor_max_viajes):
                return contenedor
    
    """def obtener_barco_con_cantidad_km_recorridos(self, funcion_para_comparacion):
        id_barco_a_cantidad_km = {}
        for viaje in self.__viajes:
            barco = viaje.get_barco()
            gps = barco.get_gps()
            cantidad_km = id_barco_a_cantidad_km.get(barco.get_id())
            if (cantidad_km is None):
                id_barco_a_cantidad_km[barco.get_id()] = gps.obtener_distancia()
            else:
                cantidad_km += gps.obtener_distancia()
                id_barco_a_cantidad_km[barco.get_id()] = cantidad_km
        
        id_barco = funcion_para_comparacion(id_barco_a_cantidad_km, key = id_barco_a_cantidad_km.get) 
        return self.buscar_barco_cantidad_km_recorridos(id_barco)
    
    def obtener_barco_con_mayor_cantidad_km_recorridos(self):
        return self.obtener_barco_con_cantidad_km_recorridos(max)
    
    def obtener_barco_con_menor_cantidad_km_recorridos(self):
        return self.obtener_barco_con_cantidad_km_recorridos(min)"""
    
    def buscar_barco_cantidad_km_recorridos(self, id_barco):
        for barco in self.__barcos:
            if barco.get_id() == id_barco:
                return barco
        return None
    
    def obtener_cantidad_km_recorridos_por_barco(self):
        id_barco_a_cantidad_km = {}

        for viaje in self.__viajes:
            barco = viaje.get_barco()
            gps = barco.get_gps()
            cantidad_km = id_barco_a_cantidad_km.get(barco.get_id(), 0)
            cantidad_km += gps.obtener_distancia()
            id_barco_a_cantidad_km[barco.get_id()] = cantidad_km

        return id_barco_a_cantidad_km
    
    def obtener_barco_con_mayor_cantidad_km_recorridos(self):
        id_barco_a_cantidad_km = self.obtener_cantidad_km_recorridos_por_barco()
        id_barco = max(id_barco_a_cantidad_km, key = id_barco_a_cantidad_km.get)
        return self.buscar_barco_cantidad_km_recorridos(id_barco)
    
    def obtener_barco_con_menor_cantidad_km_recorridos(self):
        id_barco_a_cantidad_km = self.obtener_cantidad_km_recorridos_por_barco()
        id_barco = min(id_barco_a_cantidad_km, key = id_barco_a_cantidad_km.get)
        return self.buscar_barco_cantidad_km_recorridos(id_barco)