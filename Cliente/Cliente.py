from Mercaderia.Mercaderia import Mercaderia
from Pedido.Pedido import Pedido


class Cliente:
    def __init__(self,nombre,id_cliente):
        self._nombre = nombre
        self._id_cliente = id_cliente
        self.pedido = set()

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id_cliente(self):
        return self.id_cliente                                                                                                                                                                                                                       

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def get_pedido(self):
        return self.pedido

    def set_pedido(self, pedido):
        self.pedido = pedido

    def datos_mercaderia(self):
        print("Ingrese los datos de su mercadería")
        dim_ext_al = float(input("Ingresar altura: "))
        dim_ext_an = float(input("Ingresar ancho: "))
        dim_ext_la = float(input("Ingresar largo: "))
        peso = float(input("Ingresar peso: "))
        es_especial = bool(input("Ingresar si es especial (True/False): "))

        aux_merca = Mercaderia(es_especial, dim_ext_an, dim_ext_al, dim_ext_la, peso)

        return aux_merca

    def datos_pedido(self):
        print("Ingrese los datos de su pedido")
        destino = float(input("Destino de la mercadería: "))
        servicio_completo = bool(input("Quiere servicio puerta a puerta? (True/False): "))

        aux_pedido = Pedido(self.datos_mercaderia(), self, destino, servicio_completo)

        return aux_pedido
    
