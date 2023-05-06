#from Contenedor.Contenedor import Contenedor

class Pedido:
   
   def restoCon(self, number):
        resto = number % 100

        cant_cien_kilos = 0

        if resto == 0:
            cant_cien_kilos = number // 100  # 300 // 100 = 3; 3*1000
        else:
            cant_cien_kilos = number // 100 + 1  # 469 // 100 = 4 + 1

        return cant_cien_kilos
   """ def __init__(self):
        self.mercaderia = None
        self.cliente = None
        self.destino = 0.0
        self.servicioCompleto = False

    def getMercaderia(self):
        return self.mercaderia

    def setMercaderia(self, mercaderia):
        self.mercaderia = mercaderia

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def getDestino(self):
        return self.destino

    def setDestino(self, destino):
        self.destino = destino

    def getServicioCompleto(self):
        return self.servicioCompleto

    def setServicioCompleto(self, servicioCompleto):
        self.servicioCompleto = servicioCompleto


"""

"""
   ## def precioPedido(self, contenedor: Contenedor):
        precioContenedor = 1
        precioCamion = 1
        cant_cien_kilos = 0

        # VER SI USA CAMION
        if self.servicioCompleto:
            precioCamion = 20000

        # CALCULAR CANTIDAD DE 100KG DEL CONTENEDOR
        resto = contenedor.get_peso_ocupado() % 100
        if resto == 0:
            cant_cien_kilos = contenedor.get_peso_ocupado() // 100  # 300 // 100 = 3; 3*1000
        else:
            cant_cien_kilos = contenedor.get_peso_ocupado() // 100 + 1  # 469 // 100 = 4 + 1

        # LOGICA
        # 100
        if self.destino < 100 and contenedor.get_completo():
            precioContenedor = 200000
        elif self.destino < 100 and not contenedor.get_completo():
            precioContenedor = cant_cien_kilos * 1000

        # 1000
        if 100 <= self.destino < 1000 and contenedor.get_completo():
            precioContenedor = 210000
        elif 100 <= self.destino < 1000 and not contenedor.get_completo():
            precioContenedor = cant_cien_kilos * 1100

        # 10000
        if 1000 <= self.destino < 10000 and contenedor.get_completo():
            precioContenedor = 230000
        elif 1000 <= self.destino < 10000 and not contenedor.get_completo():
            precioContenedor = cant_cien_kilos * 1150

        # 100000
        if self.destino >= 10000 and contenedor.get_completo():
            precioContenedor = 250000
        elif self.destino >= 10000 and not contenedor.get_completo():
            precioContenedor = cant_cien_kilos * 1500

        # FINAL
        return precioContenedor * precioCamion

        """