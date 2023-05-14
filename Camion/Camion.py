from Contenedor.Contenedor import Contenedor


class Camion:
    def __init__(self):
        self.id = 0
        self.precio = 20000
        self.carga = []
    
    def set_id(self, id):
        self._id = id

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def get_carga(self):
        return self._carga

    def set_carga(self, carga):
        self._carga = carga


    def cargar_camion(self, contenedor: Contenedor):
        self.carga.append(contenedor)

    def descargar_camion(self, contenedor: Contenedor):
        self.carga.remove(contenedor)
