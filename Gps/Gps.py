class Gps():
    def __init__(self) -> None:
        pass

    def calcular_distancia(self, pedido):
        distancia = pedido.get_destino()    
        return distancia

    def obtener_distancia(self):
        return self.calcular_distancia()