
class Calculador_Precio_Pedido():


     def calcular_kilos(self, number):
        resto = number % 100
        cant_cien_kilos = 0

        if resto == 0:
            cant_cien_kilos = number // 100  # 300 // 100 = 3; 3*1000
        else:
            cant_cien_kilos = number // 100 + 1  # 469 // 100 = 4 + 1


        return cant_cien_kilos



     def calcular_precio_pedido(self, pedido, contenedor, gps):
        precio_contenedor = 1
        precio_camion = pedido.usa_camion()
        c_completo = contenedor.esta_completo()
        cant_cien_kilos = self.calcular_kilos(contenedor)
        distancia = gps.calcular_distancia("origen",pedido.get_destino())

     
        # LOGICA
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

        

        return pedido.set_precio_pedido(precio_contenedor * precio_camion)

