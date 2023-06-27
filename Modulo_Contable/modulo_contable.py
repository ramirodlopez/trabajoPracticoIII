class modulo_Contable():
    
    def __init__(self, empresa):
        self.empresa = empresa
        

    def obtener_ganancia_barco_bruta(self, id):
        ganancia_barco = 0
        try:
            indice = self.empresa.get_barcos().index(id)
            ganancia_barco = self.empresa.get_barcos()[indice].obtener_ganancia_barco()
                
        except ValueError:
            print("No existe ese id de barco")
            
        return ganancia_barco
         
        


    def calcular_gasto_combustible_barco(self, barco):
     return barco.get_horas_motor() * 6
    

    def calcular_ganacia_del_barco(self):
        return self.obtener_ganancia_barco_bruta() - self.calcular_gasto_combustible_barco()
    

    """
        ##################### CLASE calcular_consumo_del_barco  #####################            

            calcular_consumo_combustible_del_barco():
                cantidad_litros_viajados = barco.get_gps().tiempo_promedio() * 6 
                
                return cantidad_litros_viajados


            obtener_combustible_restante_del_barco():
                combustible_restante                              
                combustible_restante = barco.get_capacidad_tanque() - self.calcular_consumo_combustible_del_barco()

                return combustible_restante

  

    
                 
        ########################   CLASE MODULO_CONTABLE   #####################

         
         obtener_ganancia_barco_bruta(id):
            ganacia_barco = 0
            try:
                indice = self.empresa.get_barcos().index(id)
                ganacia_barco = get_barcos().[indice].obtener_ganancia_barco()
                print(f"El elemento está en el índice {indice}")
            except ValueError:
                print("El elemento no está en el array")
            
            return ganacia_barco
         
        
         
         obtener_gasto_combustible_barco(Consumo_Barco):

            return Consumo_Barco.calcular_consumo_del_barco()
         


         calcular_ganacia_del_barco():
            return self.obtener_ganancia_barco_bruta() - self.obtener_gasto_combustible_barco()



    
       ##################### CLASE BARCO #####################

         ganacia_barco = 0
         obtener_ganancia_barco(Pedido):
            for contendor in self.get_contenedores():
                    ganancia_barco += contendor.obtener_ganancia_contenedor(Pedido)

        

        ##################### CLASE BARCO #####################
        def set.estrategia(estrategia):
            self.estrategia = estrategia

        
        def do_something():
            self.estrategia.hora_de_activacion()
            #guardar en array de activaciones.

         

        ########################   CLASE CONTENEDOR  #####################

         obtener_ganancia_contenedor(Pedido):
         ganancia_contenedor
            for mercaderia in self.get_mercaderias():
                ganancia_contenedor += mercaderia.obtener_ganancia_mercaderia(mercaderia.get_id, Pedido)
                                   
        



          
          
        ########################   CLASE MERCADERIA   #####################

         obtener_ganancia_mercaderia(id_mercaderia, Pedido):    
            return ganancia_mercaderia =  pedido.obtener_ganancia_pedido(id_mercaderia)
        
            
       
    
           
          
        ########################   CLASE PEDIDO   #####################

         obtener_ganancia_pedido(id_mercaderia):
            precio_del_pedido = None
            for pedido in self.get_pedidos():
                if pedido.mercaderia.get_id_mercaderia() == id_mercaderia:
                    precio_del_pedido = pedido.get_precio_pedido()




        
         #################### ##################### #################### ####################
         ############ ##################### #################### ##################### ######



       ##################### CLASE BARCO CON VELA #####################
        
            hora_de_activacion():
                hora_cambio = datetime.datetime.now()    V: 05:56:24
                return

       ##################### CLASE BARCO CON MOTOR #####################
        
            hora_de_activacion():
                hora_cambio = datetime.datetime.now()    V: 09:56:24
                return

            tiempo_de_uso(gps):
                hora_cambio_vela = datetime.datetime.now() 05:56:24                     
                hora_cambio_vela = datetime.datetime.now() 13:56:24                     V: 05:56:24
                                                                                        M: 09:56:24
                                                                                        V: 13:56:24

                                                                                        VELATOTAL: 8HS -> V1 + V2
                                                                                        MOTORTOTAL: 8HS

       
       ##################### CLASE BARCO CON MOTOR #####################

        consumo_de_combustible():
            gasta gasoil
            
        
        tiempo_de_uso(gps):
            hora_cambio_motor = datetime.datetime.now() 09:56:24

             

    """