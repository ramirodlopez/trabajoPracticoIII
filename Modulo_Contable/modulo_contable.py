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
    

    def calcular_ganacia_del_barco(self, id, barco):
        return self.obtener_ganancia_barco_bruta(id) - self.calcular_gasto_combustible_barco(barco)
    

    