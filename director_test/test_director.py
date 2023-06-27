from unittest import TestCase
from unittest.mock import Mock

from Contenedor.Director import Director


class DirestorContainerTest(TestCase): 
    def test_crear_contenedor_basico(self):
        builder = Mock()
        director = Director()
        director.builder = builder

        contenedor = Mock()
        builder.builder.return_value = builder
        builder.asignar_largo.return_value = builder
        builder.asignar_ancho.return_value = builder
        builder.asignar_alto.return_value = builder
        builder.asignar_peso_max.return_value = builder
        builder.asignar_volumen.return_value = builder
        builder.asignar_alto_exterior.return_value = builder
        builder.asignar_largo_exterior.return_value = builder
        builder.asignar_ancho_exterior.return_value = builder
    
        builder.get_contenedor.return_value = contenedor

        resultado = director.crear_contenedor_basico(123, False)

        self.assertEqual(resultado, contenedor)
        builder.builder.assert_called_with(123, False)
        builder.asignar_largo.assert_called_with(6)
        builder.asignar_ancho.assert_called_with(2.35)
        builder.asignar_alto.assert_called_with(2.3)
        builder.asignar_peso_max.assert_called_with(24000)
        builder.asignar_volumen.assert_called_with(32.42999999999999)
        builder.asignar_alto_exterior.assert_called_with(2.6)
        builder.asignar_largo_exterior.assert_called_with(6.1)
        builder.asignar_ancho_exterior.assert_called_with(2.45)
        
    def test_crear_contenedor_basico_hc(self):
        builder = Mock()
        director = Director()
        director.builder = builder

        contenedor = Mock()
        builder.builder.return_value = builder
        builder.asignar_largo.return_value = builder
        builder.asignar_ancho.return_value = builder
        builder.asignar_alto.return_value = builder
        builder.asignar_peso_max.return_value = builder
        builder.asignar_volumen.return_value = builder
        builder.asignar_alto_exterior.return_value = builder
        builder.asignar_largo_exterior.return_value = builder
        builder.asignar_ancho_exterior.return_value = builder
    
        builder.get_contenedor.return_value = contenedor

        resultado = director.crear_contenedor_basico_hc(525, False)

        self.assertEqual(resultado, contenedor)
        builder.builder.assert_called_with(525, False)
        builder.asignar_largo.assert_called_with(12)
        builder.asignar_ancho.assert_called_with(2.35)
        builder.asignar_alto.assert_called_with(2.3)
        builder.asignar_peso_max.assert_called_with(32500)
        builder.asignar_volumen.assert_called_with(67.7)
        builder.asignar_alto_exterior.assert_called_with(2.6)
        builder.asignar_largo_exterior.assert_called_with(12.1)
        builder.asignar_ancho_exterior.assert_called_with(2.45)

    def test_crear_contenedor_flat_rack(self):
        builder = Mock()
        director = Director()
        director.builder = builder

        contenedor = Mock()
        builder.builder.return_value = builder
        builder.asignar_largo.return_value = builder
        builder.asignar_ancho.return_value = builder
        builder.asignar_alto.return_value = builder
        builder.asignar_peso_max.return_value = builder
        builder.asignar_volumen.return_value = builder
        builder.asignar_alto_exterior.return_value = builder
        builder.asignar_largo_exterior.return_value = builder
        builder.asignar_ancho_exterior.return_value = builder
    
        builder.get_contenedor.return_value = contenedor

        resultado = director.crear_contenedor_flat_rack(777, False)

        self.assertEqual(resultado, contenedor)
        builder.builder.assert_called_with(777, False)
        builder.asignar_largo.assert_called_with(6)
        builder.asignar_ancho.assert_called_with(None)
        builder.asignar_alto.assert_called_with(2.3)
        builder.asignar_peso_max.assert_called_with(45000)
        builder.asignar_volumen.assert_called_with(33)
        builder.asignar_alto_exterior.assert_called_with(2.3)
        builder.asignar_largo_exterior.assert_called_with(6.1)
        builder.asignar_ancho_exterior.assert_called_with(None)

    def test_crear_contenedor_alimenticio(self):
        builder = Mock()
        director = Director()
        director.builder = builder

        contenedor = Mock()
        builder.builder.return_value = builder
        builder.asignar_largo.return_value = builder
        builder.asignar_ancho.return_value = builder
        builder.asignar_alto.return_value = builder
        builder.asignar_peso_max.return_value = builder
        builder.asignar_volumen.return_value = builder
        builder.asignar_alto_exterior.return_value = builder
        builder.asignar_largo_exterior.return_value = builder
        builder.asignar_ancho_exterior.return_value = builder
    
        builder.get_contenedor.return_value = contenedor

        resultado = director.crear_contenedor_alimenticio(888, False)

        self.assertEqual(resultado, contenedor)
        builder.builder.assert_called_with(888, False)
        builder.asignar_largo.assert_called_with(6)
        builder.asignar_ancho.assert_called_with(2.35)
        builder.asignar_alto.assert_called_with(2.3)
        builder.asignar_peso_max.assert_called_with(24000)
        builder.asignar_volumen.assert_called_with(32.6)
        builder.asignar_alto_exterior.assert_called_with(2.6)
        builder.asignar_largo_exterior.assert_called_with(6.1)
        builder.asignar_ancho_exterior.assert_called_with(2.45)

    def test_crear_contenedor_open_top(self):
        builder = Mock()
        director = Director()
        director.builder = builder

        contenedor = Mock()
        builder.builder.return_value = builder
        builder.asignar_largo.return_value = builder
        builder.asignar_ancho.return_value = builder
        builder.asignar_alto.return_value = builder
        builder.asignar_peso_max.return_value = builder
        builder.asignar_volumen.return_value = builder
        builder.asignar_alto_exterior.return_value = builder
        builder.asignar_largo_exterior.return_value = builder
        builder.asignar_ancho_exterior.return_value = builder
        builder.asignar_valor_adicional.return_value = builder

        builder.get_contenedor.return_value = contenedor

        resultado = director.crear_contenedor_open_top(141, False)

        self.assertEqual(resultado, contenedor)
        builder.builder.assert_called_with(141, False)
        builder.asignar_largo.assert_called_with(12)
        builder.asignar_ancho.assert_called_with(2.35)
        builder.asignar_alto.assert_called_with(None)
        builder.asignar_peso_max.assert_called_with(45000)
        builder.asignar_volumen.assert_called_with(67.7)
        builder.asignar_alto_exterior.assert_called_with(2.6)
        builder.asignar_largo_exterior.assert_called_with(12.1)
        builder.asignar_ancho_exterior.assert_called_with(2.45)
        builder.asignar_valor_adicional.assert_called_with(500)

