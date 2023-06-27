from unittest import TestCase

from unittest.mock import Mock

from Consumo_Barco.consumo_barco import Consumo_Barco

class Test_Consumo_Barco(TestCase):

    def test_verificar_resultado_esperado_en_el_init(self):
        # Crear un mock para el objeto barco
        barco_mock = Mock()

        # Crear un objeto de la clase Consumo_Barco pasando el mock del barco como argumento
        consumo_barco = Consumo_Barco(barco_mock)

        self.assertEqual(consumo_barco._barco, barco_mock)


    def test_verificar_resultado_esperado_en_obtener_combustible_restante_del_barco(self):
        # Crear un mock para el objeto barco
        barco_mock = Mock()

        # Crear un objeto de la clase Consumo_Barco pasando el mock del barco como argumento
        consumo_barco = Consumo_Barco(barco_mock)

        # Configurar el comportamiento esperado del mock del barco
        barco_mock.get_capacidad_tanque.return_value = 100

        consumo_barco.calcular_consumo_combustible_del_barco = Mock(return_value=40)

        consumo_barco._barco = barco_mock

        # Ejecutar el metodo obtener_combustible_restante_del_barco()
        combustible_restante = consumo_barco.obtener_combustible_restante_del_barco()

        self.assertEqual(combustible_restante, 60)
