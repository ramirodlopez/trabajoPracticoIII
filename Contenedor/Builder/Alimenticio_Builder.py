from typing_extensions import override
from Contenedor.Alimenticio import Alimenticio
from Contenedor.Builder.Builder_Comun import BuilderComun


class BuilderAlimenticio(BuilderComun):
    def __init__(self) -> None:
        pass
    
    @override
    def reset(self, id, es_especial):
        self.contenedor = Alimenticio(id, es_especial)
        return self
    
   
    

        