from Camion.Camion import Camion
from Contenedor.Contenedor import Contenedor

class Pedido:
    def __init__(self, mercaderia, cliente, destino, servicio_completo):
        self.mercaderia = mercaderia
        self.cliente = cliente
        self.destino = destino
        self.servicio_completo = servicio_completo
        self.precio_pedido = 0

    def get_mercaderia(self):
        return self.mercaderia

    def set_mercaderia(self, mercaderia):
        self.mercaderia = mercaderia

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_destino(self):
        return self.destino

    def set_destino(self, destino):
        self.destino = destino

    def get_servicio_completo(self):
        return self.servicio_completo

    def set_servicio_completo(self, servicio_completo):
        self.servicio_completo = servicio_completo
    
    def get_precio_pedido(self):
        return self.precio_pedido

    def set_precio_pedido(self, precio_pedido):
        self.precio_pedido = precio_pedido



    
    def usa_camion(self):
        precio = 0
        if(self.get_servicio_completo):
            precio = Camion.get_precio()
       
        return precio
