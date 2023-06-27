from unittest import TestCase

from unittest.mock import Mock
from Barco.Barco import Barco
from excepcion.restriccion_excepcion import RestriccionException
from Validacion_Barco.Validar_Subir_Al_Barco_Avanzado import Validar_Subir_Al_Barco_Avanzado
from Validacion_Barco.Validar_Subir_Al_Barco_Basico import Validar_Subir_Al_Barco_Basico

class Test_Validar_Subir_Al_Barco(TestCase):

    def test_creo_contenedor_con_dimensiones_validas_y_verifico_que_contenedor_sea_basico(self):
        # Crear un objeto de restriccion
        restriccion = Validar_Subir_Al_Barco_Basico()

        # Crear un mock para el contenedor basico
        contenedor_mock = Mock()
        contenedor_mock.get_ancho_exterior.return_value = 2.45
        contenedor_mock.get_alto_exterior.return_value = 2.6
        contenedor_mock.get_largo_exterior.return_value = 6.1

        # Verificar que el contenedor sea considerado basico segun la restriccion
        assert restriccion.es_basico(contenedor_mock) == True

    def test_creo_contenedor_con_dimensiones_invalidas_y_verifico_que_contenedor_no_sea_basico(self):
        # Crear un objeto de restriccion
        restriccion = Validar_Subir_Al_Barco_Basico()

        # Crear un mock para el contenedor avanzado
        contenedor_mock = Mock()
        contenedor_mock.get_ancho_exterior.return_value = 2.46
        contenedor_mock.get_alto_exterior.return_value = 2.7
        contenedor_mock.get_largo_exterior.return_value = 6.2

        # Verificar que el contenedor no sea considerado basico segun la restriccion
        assert restriccion.es_basico(contenedor_mock) == False

    
    def test_verificar_restricciones_para_un_barco_avanzado_con_dimensiones_validas(self):
        # Crear un mock para el objeto Barco
        barco_mock = Mock()

        # Crear un mock para el objeto Contenedor
        contenedor_mock = Mock()

        # Configurar los métodos necesarios del mock de Contenedor
        contenedor_mock.get_ancho_exterior.return_value = 2.5
        contenedor_mock.get_alto_exterior.return_value = 2.7
        contenedor_mock.get_largo_exterior.return_value = 6.2

        restriccion_mock = Mock(spec=Validar_Subir_Al_Barco_Avanzado)
        restriccion_mock.verificar_restricciones_barco_generales.return_value = True

        # Crear un objeto de restriccion utilizando el mock
        restriccion = restriccion_mock

        # Verificar las restricciones
        resultado = restriccion.verificar_restricciones_barco_segun_su_tipo(barco_mock, contenedor_mock)

        # Comprobar si el resultado es True
        self.assertTrue(resultado)
        

    def test_verificar_restricciones_para_un_contenedor_en_barco_avanzado_con_cantidad_de_contenedores_excedida(self):
        contenedor = Mock()
        barco = Barco(1, 0, 5000, None)

        contenedor.get_peso_ocupado.return_value = 1000
        contenedor.get_ancho_exterior.return_value = 2.46
        contenedor.get_alto_exterior.return_value = 2.7
        contenedor.get_largo_exterior.return_value = 6.5

        restriccion = Validar_Subir_Al_Barco_Avanzado()

        barco.agregar_contenedor(contenedor, restriccion)

        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_segun_su_tipo(barco, contenedor)
