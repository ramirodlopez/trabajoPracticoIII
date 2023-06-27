class Consumo_Barco:
    def __init__(self, barco) -> None:
        self._barco = barco


    def calcular_consumo_combustible_del_barco(self):
        cantidad_litros_viajados = self._barco.get_gps().tiempo_promedio * 6

        return cantidad_litros_viajados
    
    def obtener_combustible_restante_del_barco(self):
        combustible_restante = self._barco.get_capacidad_tanque() - self.calcular_consumo_combustible_del_barco()

        return combustible_restante