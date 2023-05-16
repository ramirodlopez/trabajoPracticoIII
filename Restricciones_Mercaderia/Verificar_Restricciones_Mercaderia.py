from Excepcion.Restriccion_Excepcion import RestriccionException

class VerificarRestricciones():
    def __init__(self) -> None:
        pass

    def verificar_restricciones(self, contenedor):
        self.verificar_especial(contenedor)
        self.verificar_largo(contenedor)
        self.verificar_alto(contenedor)
        self.verificar_volumen(contenedor)
        self.verificar_ancho(contenedor)
        self.verificar_peso(contenedor)

    def verificar_especial(self, contenedor, mercaderia):
        if (mercaderia.get_es_especial() and not contenedor.is_especial()):
            raise RestriccionException("No se puede cargar una mercadería especial en este contenedor.")
    
    def verificar_alto(self, contenedor, mercaderia):
        if (not contenedor.entra_alto(mercaderia.get_alto())):
            raise RestriccionException("El alto de la mercadería es mayor que la del contenedor.")

    def verificar_largo(self, contenedor, mercaderia):
        if (mercaderia.get_largo()> contenedor.get_largo()): 
            raise RestriccionException("El largo de la mercadería es mayor que la del contenedor.")

    def verificar_volumen(self, contenedor, mercaderia):
        if (mercaderia.devolver_volumen() > contenedor.get_volumen() - contenedor.get_volumen_ocupado()): 
            raise RestriccionException("El volumen de la mercadería es mayor que la del contenedor.")

    def verificar_ancho(self, contenedor, mercaderia):
        if (not contenedor.entra_ancho(mercaderia.get_ancho())):
            raise RestriccionException("El ancho de la mercadería es mayor que la del contenedor.")

    def verificar_peso(self, contenedor, mercaderia):
        if (mercaderia.get_peso() > contenedor.get_peso_max() - contenedor.get_peso_ocupado()): 
            raise RestriccionException("El peso de la mercadería es mayor que la del contenedor.")