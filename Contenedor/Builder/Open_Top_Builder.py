from typing_extensions import override

from Contenedor.Open_Top import OpenTop
from Contenedor.Builder.Builder_Comun import BuilderComun

class BuilderOpenTop(BuilderComun):
    def __init__(self) -> None:
        pass

    @override
    def builder(self, id, es_especial):
        self.contenedor = OpenTop(id, es_especial)
        return self
    
    
        