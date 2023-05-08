from excepcion.restriccion_excepcion import RestriccionException

class Mercaderia():
    def __init__(self, esEspecial, ancho, alto, largo, peso):
        self.es__especial = esEspecial
        self.__alto = alto
        self.__largo = largo
        self.__ancho = ancho
        self.__peso = peso

    
    def verificar_restricciones(self, contenedor: 'Contenedor'):
        self.verificar_especial(contenedor)
        self.verificar_largo(contenedor)
        self.verificar_alto(contenedor)
        self.verificar_volumen(contenedor)
        self.verificar_ancho(contenedor)
        self.verificar_peso(contenedor)

    def verificar_especial(self, contenedor: 'Contenedor'):
        if (self.es__especial and not contenedor.is_especial()):
            raise RestriccionException("No se puede cargar una mercadería especial en este contenedor.")
    
    def verificar_alto(self, contenedor: 'Contenedor'):
        if (not contenedor.entra_alto(self.__alto)):
            raise RestriccionException("El alto de la mercadería es mayor que la del contenedor.")

    def verificar_largo(self, contenedor: 'Contenedor'):
        if (self.__largo > contenedor.get_largo()): 
            raise RestriccionException("El largo de la mercadería es mayor que la del contenedor.")

    def verificar_volumen(self, contenedor: 'Contenedor'):
        if (self.devolver_volumen() > contenedor.get_volumen() - contenedor.get_volumen_ocupado()): 
            raise RestriccionException("El volumen de la mercadería es mayor que la del contenedor.")

    def verificar_ancho(self, contenedor: 'Contenedor'):
        if (not contenedor.entra_ancho(self.__ancho)):
            raise RestriccionException("El ancho de la mercadería es mayor que la del contenedor.")

    def verificar_peso(self, contenedor: 'Contenedor'):
        if (self.__peso > contenedor.get_peso_max() - contenedor.get_peso_ocupado()): 
            raise RestriccionException("El peso de la mercadería es mayor que la del contenedor.")

    def get_es_especial(self):
        return self.es__especial
    def set_es_especial(self, valor):
        self.es__especial = valor

    def get_ancho(self):
        return self.__ancho
    
    def set_ancho(self, valor):
        self.__ancho = valor
    
    def get_alto(self): 
        return self.__alto
    
    def set_alto(self, valor):
        self.__alto = valor

    def get_largo(self):
        return self.__largo
    
    def set_largo(self, valor):
        self.__largo = valor

    def get_peso(self):
        return self.__peso

    def set_peso(self, valor):
        self.__peso = valor

    def devolver_volumen(self):
        return self.__alto * self.__ancho * self.__largo
