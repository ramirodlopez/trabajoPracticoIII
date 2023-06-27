from abc import ABC, abstractmethod


class Estrategia(ABC):
    def __init__(self) -> None:
        self.tipo = None

    @abstractmethod
    def get_tipo(self):
        return self.tipo

    @abstractmethod
    def hora_activacion():
        pass