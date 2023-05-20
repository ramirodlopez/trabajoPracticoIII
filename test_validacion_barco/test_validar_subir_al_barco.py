from unittest import TestCase
from Barco.Avanzado import Avanzado
from Barco.Basico import Basico
from Contenedor.BasicoHC import BasicoHC
from excepcion.restriccion_excepcion import RestriccionException
from validacion_barco.Validar_Subir_Al_Barco import Validar_Subir_Al_Barco

class Test_Validar_Subir_Al_Barco(TestCase):

    def test_verificar_restricciones_barco_basico(self):
        # Creo instancia de contenedor
        contenedor = BasicoHC(1, False)
        contenedor.set_peso_ocupado(1000)
        contenedor.set_ancho_exterior(2.45)
        contenedor.set_alto_exterior(2.6)
        contenedor.set_largo_exterior(6.1)

        # Verifico restricciones para un contenedor en un barco basico con dimensiones validas
        restriccion = Validar_Subir_Al_Barco()
        try:
            restriccion.verificar_restricciones_barco_basico(Basico(1, 10, 5000, None), contenedor)
        except RestriccionException as exception:
            self.fail(f"Se produjo una excepcion inesperada: {str(exception)}")

        # Verifico restricciones para un contenedor en un barco basico con dimensiones invalidas
        contenedor.set_ancho_exterior(2.46)
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_basico(Basico(1, 10, 5000, None), contenedor)

        contenedor.set_ancho_exterior(2.45)
        contenedor.set_alto_exterior(2.7)
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_basico(Basico(1, 10, 5000, None), contenedor)

        contenedor.set_alto_exterior(2.6)
        contenedor.set_largo_exterior(6.2)
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_basico(Basico(1, 10, 5000, None), contenedor)

        contenedor.set_largo_exterior(6.1)

        # Verifica restricciones para un contenedor en un barco basico con material especial
        contenedor.set_especial(True)
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_basico(Basico(1, 10, 5000, None), contenedor)


    def test_verificar_restricciones_barco_avanzado(self):
        contenedor = BasicoHC(1, False)
        barco = Avanzado(1, 0, 5000, None)

        # Verifico restricciones para un barco avanzado con dimensiones validas
        contenedor.set_peso_ocupado(1000)
        contenedor.set_ancho_exterior(2.46)
        contenedor.set_alto_exterior(2.7)
        contenedor.set_largo_exterior(6.5)
        restriccion = Validar_Subir_Al_Barco()
        try:
            restriccion.verificar_restricciones_barco_avanzado(barco, contenedor)
        except RestriccionException as exception:
            self.fail(f"Se produjo una excepcion inesperada: {str(exception)}")

        # Verifico restricciones para un contenedor en un barco avanzado con cantidad de contenedores excedida
        barco.agregar_contenedor(contenedor)
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_avanzado(barco, contenedor)

        # Verifico restricciones para un contenedor en un barco avanzado con peso excedido
        barco._peso_total = 50000
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_avanzado(barco, contenedor)

        

