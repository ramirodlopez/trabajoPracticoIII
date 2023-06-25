from typing_extensions import override
from Contenedor.Basico import Basico
from Contenedor.Builder.Builder_Comun import BuilderComun


class BuilderBasico(BuilderComun):
    def __init__(self) -> None:
        pass
    
    @override
    def reset(self, id, es_especial):
        self.contenedor = Basico(id, es_especial)
        return self
    