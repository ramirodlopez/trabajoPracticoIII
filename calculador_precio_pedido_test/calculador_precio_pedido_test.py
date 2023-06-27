import unittest
from unittest.mock import Mock
from calculador_precio_pedido.Calculador_Precio_Pedido import Calculador_Precio_Pedido

class TestCalculadorPrecioPedido(unittest.TestCase):
    def setUp(self):
        self.calculador = Calculador_Precio_Pedido(Mock())

    def test_calcular_kilos_exacto(self):
        resultado = self.calculador.calcular_kilos(300)
        self.assertEqual(resultado, 3)

    def test_calcular_kilos_redondeo(self):
        resultado = self.calculador.calcular_kilos(469)
        self.assertEqual(resultado, 5)

    def test_calcular_precio_pedido(self):
        self.calculador.obtener_distancia = Mock(return_value=80)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=500) #precio adicional open top.

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6500)

    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#

    #------------PARA DISTANCIAS DE 100------------
    #------------CON CONTENEDOR COMPLETO Y SIN USAR CAMION------------
    def test_calcular_precio_pedido_distancia_menor_cien_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=80)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0)
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0) 

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 200000)


    def test_calcular_precio_pedido_distancia_igual_cien_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=100)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0)
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 210000)

    
    def test_calcular_precio_pedido_distancia_mayor_cien_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=150)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0)
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 210000)

    #------------CON CONTENEDOR COMPLETO Y USANDO CAMION------------


    def test_calcular_precio_pedido_distancia_menor_cien_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=80)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000)
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 220000)


    def test_calcular_precio_pedido_distancia_igual_cien_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=100)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000)
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 230000)

    
    def test_calcular_precio_pedido_distancia_mayor_cien_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=150)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000)
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 230000)

  
     #------------CON CONTENEDOR INCOMPLETO Y SIN USAR CAMION------------

   
    def test_calcular_precio_pedido_distancia_menor_cien_y_contenedor_incompleto_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=80)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0)
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)
        
        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6000)


    def test_calcular_precio_pedido_distancia_igual_cien_y_contenedor_incompleto_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=100)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6600)

    
    def test_calcular_precio_pedido_distancia_mayor_cien_y_contenedor_incompleto_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=150)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6600)



     #------------CON CONTENEDOR INCOMPLETO Y USANDO CAMION------------

       
    def test_calcular_precio_pedido_distancia_menor_cien_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=80)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 26000)


    def test_calcular_precio_pedido_distancia_igual_cien_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=100)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 26600)

    
    def test_calcular_precio_pedido_distancia_mayor_cien_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=150)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 26600)


    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#

    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#

    #------------PARA DISTANCIAS DE 1000------------
    #------------CON CONTENEDOR COMPLETO Y SIN USAR CAMION------------


    def test_calcular_precio_pedido_distancia_menor_mil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=800)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 210000)


    def test_calcular_precio_pedido_distancia_igual_mil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 230000)

    
    def test_calcular_precio_pedido_distancia_mayor_mil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1500)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 230000)

    #------------CON CONTENEDOR COMPLETO Y USANDO CAMION------------


    def test_calcular_precio_pedido_distancia_menor_mil_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=800)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 230000)


    def test_calcular_precio_pedido_distancia_igual_mil_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 250000)

    
    def test_calcular_precio_pedido_distancia_mayor_mil_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1500)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 250000)

  
     #------------CON CONTENEDOR INCOMPLETO Y SIN USAR CAMION------------

   
    def test_calcular_precio_pedido_distancia_menor_mil_y_contenedor_incompleto_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=800)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6600)


    def test_calcular_precio_pedido_distancia_igual_mil_y_contenedor_incompleto_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6900)

    
    def test_calcular_precio_pedido_distancia_mayor_mil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1500)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6900)



     #------------CON CONTENEDOR INCOMPLETO Y USANDO CAMION------------

       
    def test_calcular_precio_pedido_distancia_menor_mil_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=800)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 26600)


    def test_calcular_precio_pedido_distancia_igual_mil_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 26900)

    
    def test_calcular_precio_pedido_distancia_mayor_mil_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=1500)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 26900)


    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#

    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#

    #------------PARA DISTANCIAS DE 10000------------
    #------------CON CONTENEDOR COMPLETO Y SIN USAR CAMION------------


    def test_calcular_precio_pedido_distancia_menor_diezmil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=8000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 230000)


    def test_calcular_precio_pedido_distancia_igual_diezmil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=10000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 250000)

    
    def test_calcular_precio_pedido_distancia_mayor_diezmil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=15000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 250000)

    #------------CON CONTENEDOR COMPLETO Y USANDO CAMION------------


    def test_calcular_precio_pedido_distancia_menor_diezmil_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=8000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 250000)


    def test_calcular_precio_pedido_distancia_igual_diezmil_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=10000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 270000)

    
    def test_calcular_precio_pedido_distancia_mayor_diezmil_y_contenedor_completo_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=15000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=True)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 270000)

  
     #------------CON CONTENEDOR INCOMPLETO Y SIN USAR CAMION------------

   
    def test_calcular_precio_pedido_distancia_menor_diezmil_y_contenedor_incompleto_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=8000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6900)


    def test_calcular_precio_pedido_distancia_igual_diezmil_y_contenedor_incompleto_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=10000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 9000)

    
    def test_calcular_precio_pedido_distancia_mayor_diezmil_y_contenedor_completo_sin_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=15000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 9000)



     #------------CON CONTENEDOR INCOMPLETO Y USANDO CAMION------------

       
    def test_calcular_precio_pedido_distancia_menor_diezmil_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=8000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 26900)


    def test_calcular_precio_pedido_distancia_igual_diezmil_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=10000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 29000)
 
    
    def test_calcular_precio_pedido_distancia_mayor_diezmil_y_contenedor_incompleto_con_camion(self):
        self.calculador.obtener_distancia = Mock(return_value=15000)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=20000) #valor $20000 si usa $0 si no.
        self.calculador.obtener_con_completo = Mock(return_value=False)
        self.calculador.obtener_precio_adicional = Mock(return_value=0)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 29000)


    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------#


