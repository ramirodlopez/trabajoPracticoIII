class RestriccionException(Exception):
    def __init__(self, mensaje):
        self.__mensaje = mensaje
    
    def __str__(self):
        return self.__mensaje