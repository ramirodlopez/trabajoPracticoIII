from Barco.Barco import Barco
from Contenedor.Contenedor import Contenedor
from Mercaderia.Mercaderia import Mercaderia


class Basico(Barco):
    
    def agregar_contenedor(self, contenedor: Contenedor, mercaderia : Mercaderia):
        
        if (self._peso <= self._peso_max_sopor and self.cant_de_cont_cargado() <= self._cant_max_cont and 
            self.validar_disenio(contenedor) and not self.contenedor_con_material_especial(contenedor, mercaderia)):
            
            self._contenedores.add(contenedor)
        else :
            self._peso -= contenedor.get_peso_ocupado()