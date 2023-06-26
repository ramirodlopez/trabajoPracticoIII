from Excepcion.restriccion_excepcion import RestriccionException
from trabajoPracticoIII.Mercaderia.Tipo_Mercaderia import TipoMercaderia

class VerificarRestricciones():
    def __init__(self) -> None:
        pass

    def verificar_restricciones(self, contenedor, mercaderia):
        self.verificar_especial(contenedor, mercaderia)
        self.verificar_largo(contenedor, mercaderia)
        self.verificar_alto(contenedor, mercaderia)
        self.verificar_volumen(contenedor, mercaderia)
        self.verificar_ancho(contenedor, mercaderia)
        self.verificar_peso(contenedor, mercaderia)
        self.verificar_tipo_mercaderia(contenedor, mercaderia)
        self.verificar_alimentos_con_quimicos(contenedor, mercaderia)

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
        
    def verificar_tipo_mercaderia(self, contenedor, mercaderia):
        if (not contenedor.puede_contener_tipo_mercaderia(mercaderia.get_tipo_mercaderia())):
            raise RestriccionException("Las mercaderías alimenticias deben viajar en containers de tipo alimenticio.")

    def verificar_alimentos_con_quimicos(contenedor, mercaderia):
        if (TipoMercaderia.ALIMENTICIO == mercaderia.get_tipo_mercaderia()):
            mercaderias_contenidas = contenedor.get_mercaderias()
            for mercaderia_contenida in mercaderias_contenidas:
                if (TipoMercaderia.QUIMICO == mercaderia_contenida.get_tipo_mercaderia()):
                    raise RestriccionException("Las mercaderías alimenticias no pueden viajar junto a las del tipo químicas.")
