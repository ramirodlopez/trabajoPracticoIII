from Contenedor.Builder.Builder import Builder


class Director():
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self.builder
        
    @builder.setter
    def builder(self, builder):
        self._builder = builder 
    
    def crear_contenedor_basico(self, id, es_especial):
        return self._builder\
            .builder(id, es_especial)\
            .asignar_largo(6)\
            .asignar_ancho(2.35)\
            .asignar_alto(2.3)\
            .asignar_peso_max(24000)\
            .asignar_volumen(32.42999999999999)\
            .asignar_alto_exterior(2.6)\
            .asignar_largo_exterior(6.1)\
            .asignar_ancho_exterior(2.45)\
            .get_contenedor()

    def crear_contenedor_basico_hc(self, id, es_especial):
        return self._builder\
            .builder(id, es_especial)\
            .asignar_largo(12)\
            .asignar_ancho(2.35)\
            .asignar_alto(2.3)\
            .asignar_peso_max(32500)\
            .asignar_volumen(67.7)\
            .asignar_alto_exterior(2.6)\
            .asignar_largo_exterior(12.1)\
            .asignar_ancho_exterior(2.45)\
            .get_contenedor()
    

    def crear_contenedor_flat_rack(self, id, es_especial):
        return self._builder\
            .builder(id, es_especial)\
            .asignar_largo(6)\
            .asignar_ancho(None)\
            .asignar_alto(2.3)\
            .asignar_peso_max(45000)\
            .asignar_volumen(33)\
            .asignar_alto_exterior(2.3)\
            .asignar_largo_exterior(6.1)\
            .asignar_ancho_exterior(None)\
            .get_contenedor()

    def crear_contenedor_alimenticio(self, id, es_especial):
        return self._builder\
            .builder(id, es_especial)\
            .asignar_largo(6)\
            .asignar_ancho(2.35)\
            .asignar_alto(2.3)\
            .asignar_peso_max(24000)\
            .asignar_volumen(32.6)\
            .asignar_alto_exterior(2.6)\
            .asignar_largo_exterior(6.1)\
            .asignar_ancho_exterior(2.45)\
            .get_contenedor()

    def crear_contenedor_open_top(self, id, es_especial):
        return self._builder\
            .builder(id, es_especial)\
            .asignar_largo(12)\
            .asignar_ancho(2.35)\
            .asignar_alto(None)\
            .asignar_peso_max(45000)\
            .asignar_volumen(67.7)\
            .asignar_alto_exterior(2.6)\
            .asignar_largo_exterior(12.1)\
            .asignar_ancho_exterior(2.45)\
            .asignar_valor_adicional(500)\
            .get_contenedor()