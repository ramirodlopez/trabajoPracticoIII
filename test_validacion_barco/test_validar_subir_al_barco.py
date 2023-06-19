from unittest import TestCase
from Barco.Avanzado import Avanzado
from Contenedor.BasicoHC import BasicoHC
from Contenedor.Flat_Rack import FlatRack
from Excepcion.restriccion_excepcion import RestriccionException
from Validacion_Barco.Validar_Subir_Al_Barco import Validar_Subir_Al_Barco

class Test_Validar_Subir_Al_Barco(TestCase):

    def test_creo_contenedor_con_dimensiones_validas_y_verifico_que_contenedor_sea_basico(self):
        restriccion = Validar_Subir_Al_Barco()

        contenedor = BasicoHC(1, False)
        contenedor.set_peso_ocupado(1000)
        contenedor.set_ancho_exterior(2.45)
        contenedor.set_alto_exterior(2.6)
        contenedor.set_largo_exterior(6.1)

        assert restriccion.es_basico(contenedor) == True

    def test_creo_contenedor_con_dimensiones_invalidas_y_verifico_que_contenedor_no_sea_basico(self):
        restriccion = Validar_Subir_Al_Barco()
        contenedor = FlatRack(2, False)

        contenedor.set_peso_ocupado(1500)
        contenedor.set_ancho_exterior(2.46)
        contenedor.set_alto_exterior(2.7)
        contenedor.set_largo_exterior(6.2)

        assert restriccion.es_basico(contenedor) == False

    
    def test_verificar_restricciones_para_un_barco_avanzado_con_dimensiones_validas(self):
        contenedor = BasicoHC(1, False)
        barco = Avanzado(1, 0, 5000, None)

        contenedor.set_peso_ocupado(1000)
        contenedor.set_ancho_exterior(2.46)
        contenedor.set_alto_exterior(2.7)
        contenedor.set_largo_exterior(6.5)
        restriccion = Validar_Subir_Al_Barco()
        try:
            restriccion.verificar_restricciones_barco_avanzado(barco, contenedor)
        except RestriccionException as exception:
            self.fail(f"Se produjo una excepcion inesperada: {str(exception)}")

    def test_verificar_restricciones_para_un_contenedor_en_barco_avanzado_con_cantidad_de_contenedores_excedida(self):
        contenedor = BasicoHC(1, False)
        barco = Avanzado(1, 0, 5000, None)

        contenedor.set_peso_ocupado(1000)
        contenedor.set_ancho_exterior(2.46)
        contenedor.set_alto_exterior(2.7)
        contenedor.set_largo_exterior(6.5)
        restriccion = Validar_Subir_Al_Barco()
        barco.agregar_contenedor(contenedor)

        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_avanzado(barco, contenedor)
        

