from Contenedor.Contenedor import Contenedor

class Barco:
    def __init__(self, id, cant_max_cont, peso_max_sopor, peso):
        self.id = id
        self.cant_max_cont = cant_max_cont
        self.pesoMaxSopor = peso_max_sopor
        self.contenedores = set()
        self.peso = peso

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_cant_max_cont(self):
        return self.cant_max_cont

    def set_cant_maxCont(self, cant_max_cont):
        self.cant_max_Cont = cant_max_cont

    def get_peso_max_sopor(self):
        return self.peso_max_sopor

    def set_peso_max_sopor(self, peso_max_sopor):
        self.peso_max_sopor = peso_max_sopor

    def calcular_peso_cargado(self, contenedor: Contenedor):
        self.peso += contenedor.get_peso_ocupado()

    def cant_de_cont_cargado(self):
        return len(self.contenedores)

    def cargar_container(self, contenedor: Contenedor):
        if self.calcular_peso_cargado() <= self.peso_max_sopor and self.cant_de_cont_cargado() <= self.cant_max_cont:
            self.contenedores.add(contenedor)

    def descargar_container(self):
        self.contenedores.clear()

    def verificar_restricciones(self, contenedor: Contenedor):
        if self.cant_de_cont_cargado() > self.cant_max_cont:
            raise ValueError("Un barco no puede cargar más containers del máximo definido")

        if self.peso > self.peso_max_sopor:
            raise ValueError("Un barco no puede cargar más peso del máximo definido")

