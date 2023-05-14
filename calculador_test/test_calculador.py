from unittest import TestCase
from calculador_precio_pedido.Calculador_Precio_Pedido import Calculador_Precio_Pedido



class CalculadorPrecioPedidoTestCase(TestCase):
    def test_calcular_kilos(self):
        calculador = Calculador_Precio_Pedido()
        numero = 469  # Define el número para la prueba aquí
        

        resultado_esperado = 6  # Define el resultado esperado aquí
        
        resultado_actual = calculador.calcular_kilos(numero)

        self.assertEqual(resultado_actual, resultado_esperado)

