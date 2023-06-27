import datetime
from Estrategia.Estrategia import Estrategia


class Estrategia_Motor(Estrategia):
    def __init__(self) -> None:
        self.tipo = "Motor"

    def get_tipo(self):
        return self.tipo


    def hora_activacion():
        hora_activacion = datetime.datetime.now()
        return hora_activacion.hour
