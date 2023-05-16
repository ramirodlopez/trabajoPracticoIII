class Viaje():
    def __init__(self, barco, destino, estado):
        self.__barco = barco
        self.__destico = destino 
        self.__estado = estado 

    def get_barco(self):
        return self.__barco    

    def get_destino(self):
        return self.__destico

    def get_estado(self):
        return self.__estado