

class Contenedor:
    def __init__(self):
        self.completo = None
        self.peso_ocupado = None
        self.peso_max = None
        self.volumen_ocupado = None
        self.volumen = None
    

    def get_completo(self):
        return self._completo
    
    completo.setter
    def completo(self, value):
        self._completo = value
    

    def get_peso_ocupado(self):
        return self._peso_ocupado
    
    peso_ocupado.setter
    def peso_ocupado(self, value):
        self._peso_ocupado = value
    

    def get_peso_max(self):
        return self._peso_max
    
    peso_max.setter
    def peso_max(self, value):
        self._peso_max = value
    
 
    def get_volumen_ocupado(self):
        return self._volumen_ocupado
    
    volumen_ocupado.setter
    def volumen_ocupado(self, value):
        self._volumen_ocupado = value
    
  
    def get_volumen(self):
        return self._volumen
    
    volumen.setter
    def volumen(self, value):
        self._volumen = value
        
    def verificar_completo(self):
        if self.peso_ocupado == self.peso_max or self.volumen_ocupado == self.volumen:
            self.completo = True