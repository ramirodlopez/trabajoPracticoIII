



class Calculador_Precio_Pedido():


     def calcular_kilos(self, number):
        resto = number % 100
        cant_cien_kilos = 0

        if resto == 0:
            cant_cien_kilos = number // 100  # 300 // 100 = 3; 3*1000
        else:
            cant_cien_kilos = number // 100 + 1  # 469 // 100 = 4 + 1


        return cant_cien_kilos



     def calcular_precio_pedido(self, pedido, contenedor):
        precio_contenedor = 1
        precio_camion = 1
        cant_cien_kilos = self.calcular_kilos(contenedor)

        # VER SI USA CAMION
        if pedido.servicio_completo:
            precio_camion = 20000

        # LOGICA
        if pedido.get_destino() < 100:
            if contenedor.esta_completo():
                precio_contenedor = 200000
            else:
                precio_contenedor = cant_cien_kilos * 1000

        elif 100 <= pedido.get_destino() < 1000:
            if contenedor.esta_completo():
                precio_contenedor = 210000
            else:
                precio_contenedor = cant_cien_kilos * 1100

        elif 1000 <= pedido.get_destino() < 10000:
            if contenedor.esta_completo():
                precio_contenedor = 230000
            else:
                precio_contenedor = cant_cien_kilos * 1150

        else:
            if contenedor.esta_completo():
                precio_contenedor = 250000
            else:
                precio_contenedor = cant_cien_kilos * 1500

        return precio_contenedor * precio_camion

    
