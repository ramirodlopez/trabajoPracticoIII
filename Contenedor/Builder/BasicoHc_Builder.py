from typing_extensions import override
from Contenedor.BasicoHC import BasicoHC
from Contenedor.Builder.Builder_Comun import BuilderComun


class BuilderBasicoHc(BuilderComun):
    def __init__(self) -> None:
        pass
    
    @override
    def reset(self, id, es_especial):
        self.contenedor = BasicoHC(id, es_especial)
        return self
    
    
    

        