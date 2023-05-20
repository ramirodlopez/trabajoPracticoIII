from unittest import TestCase
from Barco.Basico import Basico
from Barco.Avanzado import Avanzado
from Contenedor.BasicoHC import BasicoHC
from Contenedor.flat_rack import FlatRack
from excepcion.restriccion_excepcion import RestriccionException
from Gps.Gps import Gps
from validacion_barco.Validar_Subir_Al_Barco import Validar_Subir_Al_Barco

class Test_Barco(TestCase):

    def test_init(self):
        gps = Gps()

        barco = Basico(1, 10, 5000, gps)

        self.assertEqual(barco._id, 1)
        self.assertEqual(barco._cant_max_cont, 10)
        self.assertEqual(barco._peso_max_sopor, 5000)
        self.assertEqual(barco._contenedores, set())
        self.assertEqual(barco._peso_total, 0)
        self.assertEqual(barco._gps, gps)


    def test_calcular_peso_cargado(self):
        barco = Avanzado(1, 10, 10000, None)

        contenedor1 = BasicoHC(1, False)
        contenedor2 = BasicoHC(2, False)
        contenedor3 = BasicoHC(3, False)

        contenedor1.set_peso_ocupado(5000)
        barco.calcular_peso_cargado(contenedor1)
        assert barco.get_peso_total() == 5000

        contenedor2.set_peso_ocupado(2500)
        barco.calcular_peso_cargado(contenedor2)
        assert barco.get_peso_total() == 7500

        contenedor3.set_peso_ocupado(3500)
        barco.calcular_peso_cargado(contenedor3)
        assert barco.get_peso_total() == 11000


    def test_contar_contenedores(self):
        barco = Basico(1, 10, 5000, None)
        contenedor1 = BasicoHC(1, False)
        contenedor2 = BasicoHC(2, False)
        contenedor3 = BasicoHC(3, False)

        assert barco.contar_contenedores() == 0

        contenedor1.set_peso_ocupado(1000)
        contenedor1.set_ancho_exterior(2.45)
        contenedor1.set_alto_exterior(2.6)
        contenedor1.set_largo_exterior(6.1)
        barco.agregar_contenedor(contenedor1)
        assert barco.contar_contenedores() == 1

        contenedor2.set_peso_ocupado(1000)
        contenedor2.set_ancho_exterior(2.45)
        contenedor2.set_alto_exterior(2.6)
        contenedor2.set_largo_exterior(6.1)
        barco.agregar_contenedor(contenedor2)
        assert barco.contar_contenedores() == 2

        contenedor3.set_peso_ocupado(1000)
        contenedor3.set_ancho_exterior(2.45)
        contenedor3.set_alto_exterior(2.6)
        contenedor3.set_largo_exterior(6.1)
        barco.agregar_contenedor(contenedor3)
        assert barco.contar_contenedores() == 3


    def test_es_basico(self):
        barco = Basico(1, 10, 5000, None)

        # Crea un contenedor con dimensiones validas
        contenedor1 = BasicoHC(1, False)
        contenedor1.set_peso_ocupado(1000)
        contenedor1.set_ancho_exterior(2.45)
        contenedor1.set_alto_exterior(2.6)
        contenedor1.set_largo_exterior(6.1)

        # Crea un contenedor con dimensiones invalidas
        contenedor2 = FlatRack(2, False)
        contenedor2.set_peso_ocupado(1500)
        contenedor2.set_ancho_exterior(2.46)
        contenedor2.set_alto_exterior(2.7)
        contenedor2.set_largo_exterior(6.2)


        # Verifica que el contenedor que sea basico para la validacion
        assert barco.es_basico(contenedor1) == True

        # Verifica que el contenedor que no sea basico no pase la validacion
        assert barco.es_basico(contenedor2) == False

    def test_agregar_contenedor(self):
        barco = Basico(1, 10, 5000, None)

        contenedor1 = BasicoHC(1, False)
        contenedor2 = BasicoHC(2, False)
        contenedor3 = BasicoHC(3, False)
        contenedor4 = FlatRack(4, True)

        # Agrega el primer contenedor que deberia ser exitoso
        contenedor1.set_peso_ocupado(1000)
        contenedor1.set_ancho_exterior(2.45)
        contenedor1.set_alto_exterior(2.6)
        contenedor1.set_largo_exterior(6.1)
        barco.calcular_peso_cargado(contenedor1)
        barco.agregar_contenedor(contenedor1)
        assert barco.contar_contenedores() == 1

        # Agrega el segundo contenedor que tambien deberia ser exitoso
        contenedor2.set_peso_ocupado(1500)
        contenedor2.set_ancho_exterior(2.45)
        contenedor2.set_alto_exterior(2.6)
        contenedor2.set_largo_exterior(6.1)
        barco.calcular_peso_cargado(contenedor2)
        barco.agregar_contenedor(contenedor2)
        assert barco.contar_contenedores() == 2

        #Agrega el tercer contenedor que deberia fallar, ya que supera la cantidad permitida
        contenedor3.set_peso_ocupado(3000)
        contenedor3.set_ancho_exterior(2.45)
        contenedor3.set_alto_exterior(2.6)
        contenedor3.set_largo_exterior(6.1)
        barco.calcular_peso_cargado(contenedor3)
        restriccion = Validar_Subir_Al_Barco()
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_basico(barco, contenedor3)


        # Agrega el cuarto contenedor q deberia fallar, ya que contiene material especial y no se permite
        contenedor4.set_peso_ocupado(2500)
        contenedor4.set_ancho_exterior(2.45)
        contenedor4.set_alto_exterior(2.6)
        contenedor4.set_largo_exterior(6.1)
        barco.calcular_peso_cargado(contenedor3)
        barco.calcular_peso_cargado(contenedor4)
        with self.assertRaises(RestriccionException):
            restriccion.verificar_restricciones_barco_basico(barco, contenedor4)