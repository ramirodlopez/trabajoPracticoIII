import unittest
from unittest.mock import Mock
from Modulo_Contable.modulo_contable import modulo_Contable

class ModuloContableTests(unittest.TestCase):
    def test_obtener_ganancia_barco_bruta_existente(self):
        empresa_mock = Mock()
        barco_mock = Mock()
        barco_mock.obtener_ganancia_barco.return_value = 1000
        
        empresa_mock.get_barcos.return_value = [barco_mock]
        
        modulo_contable = modulo_Contable(empresa_mock)
        ganancia = modulo_contable.obtener_ganancia_barco_bruta(123)
        
        self.assertEqual(ganancia, 1000)
       
        
    def test_obtener_ganancia_barco_bruta_no_existente(self):
        empresa_mock = Mock()
        empresa_mock.get_barcos.return_value = []
        
        modulo_contable = modulo_Contable(empresa_mock)
        ganancia = modulo_contable.obtener_ganancia_barco_bruta(123)
        
        self.assertEqual(ganancia, 0)
        
        
    def test_calcular_gasto_combustible_barco(self):
        barco_mock = Mock()
        barco_mock.get_horas_motor.return_value = 10
        
        modulo_contable = modulo_Contable(Mock())
        gasto = modulo_contable.calcular_gasto_combustible_barco(barco_mock)
        
        self.assertEqual(gasto, 60)
      