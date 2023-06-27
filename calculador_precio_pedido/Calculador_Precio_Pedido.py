from Pedido.Pedido import Pedido
from Contenedor.Contenedor import Contenedor
from Gps.Gps import Gps

class Calculador_Precio_Pedido():
    
    def __init__(self, pedido):
        self.pedido = pedido
        


    def calcular_kilos(self, number):
        resto = number % 100
        cant_cien_kilos = 0

        if resto == 0:
            cant_cien_kilos = number // 100  # 300 // 100 = 3; 3*1000
        else:
            cant_cien_kilos = number // 100 + 1  # 469 // 100 = 4 + 1


        return cant_cien_kilos

    def obtener_distancia(self,gps):
        distancia = gps.calcular_distancia("origen",self.get_destino())
        return distancia
     
    def obtener_usa_camion(self):
         usa_camion = self.usa_camion()
         if(usa_camion):
             return 20000
         else:
             return 0
    
    def obtener_can_kilos(self,contenedor):
         return self.calcular_kilos(contenedor)
     
    def obtener_con_completo(self,contenedor):
          c_completo = contenedor.esta_completo()
          if(c_completo):
                return True
          else:
                return False
          
    def obtener_precio_adicional(self,contenedor):
         return contenedor.valor_adicional()


    def calcular_precio_pedido(self):
        precio_contenedor = 0
        distancia = self.obtener_distancia()
        cant_cien_kilos = self.obtener_can_kilos()
        precio_camion = self.obtener_usa_camion()
        c_completo = self.obtener_con_completo()
        precio_adicional = self.obtener_precio_adicional()


        if distancia < 100:
            if c_completo:
                precio_contenedor = 200000
            else:
                precio_contenedor = cant_cien_kilos * 1000

        elif 100 <= distancia < 1000:
            if c_completo:
                precio_contenedor = 210000
            else:
                precio_contenedor = cant_cien_kilos * 1100

        elif 1000 <= distancia < 10000:
            if c_completo:
                precio_contenedor = 230000
            else:
                precio_contenedor = cant_cien_kilos * 1150

        else:
            if c_completo:
                precio_contenedor = 250000
            else:
                precio_contenedor = cant_cien_kilos * 1500

        

        return precio_contenedor + precio_camion + precio_adicional

  