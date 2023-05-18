import unittest
from unittest.mock import Mock
from calculador_precio_pedido.Calculador_Precio_Pedido import Calculador_Precio_Pedido

class TestCalculadorPrecioPedido(unittest.TestCase):
    def setUp(self):
        self.calculador = Calculador_Precio_Pedido()

    def test_calcular_kilos_exacto(self):
        resultado = self.calculador.calcular_kilos(300)
        self.assertEqual(resultado, 3)

    def test_calcular_kilos_redondeo(self):
        resultado = self.calculador.calcular_kilos(469)
        self.assertEqual(resultado, 5)

    def test_calcular_precio_pedido(self):
        self.calculador.obtener_distancia = Mock(return_value=80)
        self.calculador.obtener_can_kilos = Mock(return_value=6)
        self.calculador.obtener_usa_camion = Mock(return_value=0)
        self.calculador.obtener_con_completo = Mock(return_value=False)

        resultado = self.calculador.calcular_precio_pedido()

        self.assertEqual(resultado, 6000)

        # Verificar llamadas a los métodos auxiliares
        self.calculador.obtener_distancia.assert_called_once()
        self.calculador.obtener_can_kilos.assert_called_once()
        self.calculador.obtener_usa_camion.assert_called_once()
        self.calculador.obtener_con_completo.assert_called_once()

if __name__ == '__main__':
    unittest.main()
