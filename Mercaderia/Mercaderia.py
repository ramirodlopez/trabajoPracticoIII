
class Mercaderia():
    def __init__(self, ancho, alto, largo, peso, id, tipo_mercaderia):
        self.__alto = alto
        self.__largo = largo
        self.__ancho = ancho
        self.__peso = peso
        self.__id = id
        self.__tipo_mercaderia = tipo_mercaderia
       
    def set_tipo_mercaderia(self, tipo_mercaderia):
        self.__tipo_mercaderia = tipo_mercaderia
    
    def get_tipo_mercaderia(self):
        return self.__tipo_mercaderia

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

    def get_id(self):
        return self.__id
    
    def set_id(self, valor):
        self.__id = valor

    def devolver_volumen(self):
        return self.__alto * self.__ancho * self.__largo


    def __eq__(self, otra_instancia: object) -> bool:
        resultado = False
        if isinstance(otra_instancia, Mercaderia):
            resultado = self.__id == otra_instancia.__id 
        return resultado

    def __hash__(self):
        return hash(self.__id)
    
    def obtener_ganancia_mercaderia(id_mercaderia, pedido):  
        ganancia_mercaderia = 0.0  
        ganancia_mercaderia =  pedido.obtener_ganancia_pedido(id_mercaderia)
        return ganancia_mercaderia