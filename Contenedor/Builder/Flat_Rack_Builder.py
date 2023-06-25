from typing_extensions import override

from Contenedor.Flat_Rack import FlatRack
from Contenedor.Builder.Builder_Comun import BuilderComun

class BuilderFlatRack(BuilderComun):
    def __init__(self) -> None:
        pass
    
    @override
    def reset(self, id, es_especial):
        self.contenedor = FlatRack(id, es_especial)
        return self
    
    
    

        